#!/usr/bin/env python

import argparse
import sys
import json

from src import analysis, data, robot


TARGETS = {
    "robot": robot.Robot,
    "robot_client": robot.RobotClient,
    "clean_data": data.clean_gps,
    "report": analysis.Report,
    "visualize": analysis.visualize_all,
    "test": data.clean_gps
}

CONFIGS = {
    "robot": "config/robot_sim.json",
    "robot_client": "config/robot_client.json",
    "clean_data": "config/clean_gps_and_imu_data.json",
    "report": "config/evaluation.json",
    "visualize": "config/visualization.json",
    "test": "config/test.json"
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
