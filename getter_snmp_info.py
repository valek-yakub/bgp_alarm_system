#!/usr/bin/env python


import json
from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen


"""
    OID 1.3.6.1.2.1.15.6.1.3 prefixes
    OID 1.3.6.1.2.1.15.6.1.2 masks
    OID 1.3.6.1.2.1.15.6.1.1 next hops
"""


# BGP OIDs
_SNMP_OIDS = {
    "prefixes": (1, 3, 6, 1, 2, 1, 15, 6, 1, 3),
    "masks": (1, 3, 6, 1, 2, 1, 15, 6, 1, 2),
    "next_hop": (1, 3, 6, 1, 2, 1, 15, 6, 1, 1)
}

_SNMP_CREDENTIAL = {
    "username": "admin",
    "authKey": "admin",
    "privKey": "admin"
}

_DEVICE = {
    "name": "Test_Switch",
    "ip_address": "1.1.1.1",
    "credential": _SNMP_CREDENTIAL,
    "udp_port": 161
}


def get_snmp_info(device_info: dict) -> tuple:
    """Get bgp prefixes info from the switches"""
    prefixes_info = cmdgen.CommandGenerator().bulkCmd(
        cmdgen.UsmUserData(
            device_info["credential"]["username"],
            authKey=device_info["credential"]["authKey"],
            privKey=device_info["credential"]["privKey"],
            authProtocol=usmHMACSHAAuthProtocol,
            privProtocol=usmDESPrivProtocol
        ),
        UdpTransportTarget((
            device_info["ip_address"],
            device_info["udp_port"]
        )),
        0, 500,
        _SNMP_OIDS["prefixes"],
        _SNMP_OIDS["masks"],
        _SNMP_OIDS["next_hop"]
    )

    return prefixes_info


def primary_data_processing(prefixes_info: tuple) -> list or int:
    """Process prefixes info firstly and return processing list"""
    error_indication, error_status, error_index, var_binds = prefixes_info

    # TODO: Logging in case of being errors in this block
    if error_indication:
        print(error_indication)
        return 1

    elif error_status:
        print(f"{error_status.prettyPrint()} at "
              f"{error_index and var_binds[int(error_index) - 1][0] or '?'}")
        return 1

    else:
        prefixes_info_list = [{
            "prefix": prefix[1].prettyPrint(),
            "mask": mask[1].prettyPrint(),
            "next_hop": next_hop[1].prettyPrint()}
            for prefix, mask, next_hop in var_binds]

    return prefixes_info_list


def fetch_bgp_snmp_prefixes(device: dict) -> dict:
    """Get, process and return bgp prefixes in JSON format"""
    prefixes_info = get_snmp_info(device)
    primary_processed_prefixes_table = primary_data_processing(prefixes_info)


def main():
    # TODO: for multiple devices
    # TODO: convert result to JSON

    primary_processed_switch_prefixes_table = fetch_bgp_snmp_prefixes(_DEVICE)
    # for prefix_info in primary_processed_prefixes_table:
    #     print(f"{prefix_info['prefix'] + '/' + prefix_info['mask']:<19} {prefix_info['next_hop']:>17}")


if __name__ == "__main__":
    main()
