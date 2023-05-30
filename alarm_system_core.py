#!/usr/bin/env python


# -*- coding: UTF-8 -*-


import json
from pprint import pprint
from getter_snmp_info import fetch_bgp_snmp_prefixes


"""
    NAME
        pull_bgp_prefixes

    DESCRIPTION
        The script receives data and send ones to specified recipients.


    :return prefixes: pre-processed list of bgp prefixes

"""


def main():
    with open("config.json") as config:
        bgp_alarm_system_config = json.load(config)

    print(fetch_bgp_snmp_prefixes(
        bgp_alarm_system_config["device"],
        bgp_alarm_system_config["snmp_credentials_templates"]["Cacti"],
        bgp_alarm_system_config["snmp_oids"]
    ))


if __name__ == "__main__":
    main()
