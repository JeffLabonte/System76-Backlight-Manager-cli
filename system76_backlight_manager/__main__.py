#!/usr/bin/env python3
import os

import yaml
from cerberus import Validator

from system76_backlight_manager.battery import Battery
from system76_backlight_manager.common import read_file
from system76_backlight_manager.keyboard_backlight import KeyboardBacklight
from system76_backlight_manager.schema.configurations import (
    schema as configurations_schema,
)

CONFIGURATION_PATH = "/etc/system76-backlight-manager.conf"


def validate_configs(configurations):
    validator = Validator(configurations_schema)
    if not validator.validate(configurations):
        raise RuntimeError(validator.errors)

    if max_value := configurations.get("brightness_max_value"):
        if max_value <= configurations.get("brightness_min_value"):
            raise RuntimeError("Expect brightness_min_value to be greater than brightness_max_value")

    if yellow_threshold := configurations.get("yellow_threshold"):
        if yellow_threshold <= configurations.get("red_threshold"):
            raise RuntimeError("Expect yellow_threshold to be greater than red_threshold")


def read_configurations():
    if os.path.exists(CONFIGURATION_PATH):
        confs = yaml.load(read_file(CONFIGURATION_PATH), Loader=yaml.FullLoader)
        validate_configs(confs)
        return confs

    return {}


def main():
    config = read_configurations()

    battery = Battery()
    kb_backlight = KeyboardBacklight(context=config, battery_handler=battery)
    print("Starting Service")
    kb_backlight.run()


if __name__ == "__main__":
    main()
