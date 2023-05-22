#!/usr/bin/env python


"""
    NAME
        pull_bgp_prefixes

    DESCRIPTION
        The script receives data and send ones to specified recipients.


    :return prefixes: pre-processed list of bgp prefixes

"""


def pull_bgp_prefixes():
    """Pull prefixes: prefix, mask, next_hop, from switches, and pre-processing ones"""
    # !!!!It's mocked function!!!!!!!!!
    # TODO: full-working func
    # Statuses: 1 - present, 0 - not present
    prefixes = [
        {"prefix": "10.1.1.0", "mask": "24", "next_hop": "10.1.1.1", "status": 1},
        {"prefix": "10.1.2.0", "mask": "24", "next_hop": "10.1.2.1", "status": 1},
        {"prefix": "10.1.3.0", "mask": "24", "next_hop": "10.1.3.1", "status": 1},
        {"prefix": "10.1.4.0", "mask": "24", "next_hop": "10.1.4.1", "status": 1}
    ]
    return prefixes


def main():
    result = pull_bgp_prefixes()
    print(result)


if __name__ == "__main__":
    main()
