#!/usr/bin/env python


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

    pprint(bgp_alarm_system_config)


if __name__ == "__main__":
    main()
