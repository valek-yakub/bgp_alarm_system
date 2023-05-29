#!/usr/bin/env python

# pyasn1 == 0.4.8
import json
from pysnmp.hlapi import *
from pysnmp.entity.rfc3413.oneliner import cmdgen


def get_snmp_info(device_info: dict, credential_info: dict, snmp_oids: dict) -> tuple:
    """Get bgp prefixes info from the switch"""
    prefixes_info = cmdgen.CommandGenerator().bulkCmd(
        cmdgen.UsmUserData(
            credential_info["username"],
            authKey=credential_info["authKey"],
            privKey=credential_info["privKey"],
            authProtocol=usmHMACSHAAuthProtocol,
            privProtocol=usmDESPrivProtocol
        ),
        UdpTransportTarget((
            device_info["ip_address"],
            device_info["udp_port"]
        )),
        0, 500,
        snmp_oids["prefixes"],
        snmp_oids["masks"],
        snmp_oids["next_hop"]
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


def fetch_bgp_snmp_prefixes(device: dict, credential: dict, snmp_oids: dict) -> list:
    """Get, process and return bgp prefixes in JSON format"""
    prefixes_info = get_snmp_info(device, credential, snmp_oids)
    primary_processed_prefixes_table = primary_data_processing(prefixes_info)

    return primary_processed_prefixes_table


def main():
    # TODO: for multiple devices
    # TODO: convert result to JSON

    # primary_processed_switch_prefixes_table = fetch_bgp_snmp_prefixes(_DEVICE)
    # for prefix_info in primary_processed_prefixes_table:
    #     print(f"{prefix_info['prefix'] + '/' + prefix_info['mask']:<19} {prefix_info['next_hop']:>17}")
    pass


if __name__ == "__main__":
    main()
