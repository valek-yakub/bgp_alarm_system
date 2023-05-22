#!/usr/bin/env python
import json
"""
    NAME
        pull_bgp_prefixes

    DESCRIPTION
        The script receives data and send ones to specified recipients.


    :return prefixes: pre-processed list of bgp prefixes

"""


def main():
    data = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
        }
    }
    with open("test.json", "w") as js_file:
        json.dump(data, js_file, indent=4)


if __name__ == "__main__":
    main()
