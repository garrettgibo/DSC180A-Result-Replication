#!/usr/bin/env python

import argparse
import sys
import json

from src import data


TARGETS = {
    "test": data.clean_gps,
}

CONFIGS = {
    "test": "config/test.json",
}


def main() -> None:
    """Runs project pipeline and calls designated targets"""
    parser = argparse.ArgumentParser()
    parser.add_argument("target", choices=TARGETS.keys())
    args = parser.parse_args()

    with open(CONFIGS[args.target]) as cf:
        config = json.load(cf)

    # initiate target sequence with designated configuration
    TARGETS[args.target](**config)


if __name__ == '__main__':
    main()
