from typing import Dict

from system76_backlight_manager.common import get_laptop_model, read_file, write_file
from system76_backlight_manager.enums import Mode, Position
from system76_backlight_manager.paths.backlights import (
    FOUR_BACKLIGHT_PATH,
    ONE_BACKLIGHT_PATH,
)


class KeyboardBacklight:

    MODEL_NUMBER_BACKLIGHT_MAPPING = {
        "oryp6": ONE_BACKLIGHT_PATH,
        "oryp4": FOUR_BACKLIGHT_PATH,
        "serw11": FOUR_BACKLIGHT_PATH,
        # More to come
    }

    def __init__(self):
        self.laptop_model = get_laptop_model()
        keyboard_backlight_paths = self.MODEL_NUMBER_BACKLIGHT_MAPPING.get(
            self.laptop_model,
        )

        if keyboard_backlight_paths is None:
            raise RuntimeError(f"{self.laptop_model} is not supported by this script")

        self.max_brightness_path = keyboard_backlight_paths["max_brightness_path"]
        self.brightness_path = keyboard_backlight_paths["brightness_path"]
        self.brightness_color_paths = keyboard_backlight_paths["brightness_color"]

    def breathe(self) -> None:
        self._ramp_up()
        self._ramp_down()

    def static(self, brightness_level: int) -> None:
        if brightness_level > self.max_brightness:
            raise RuntimeError("Brightness level must not exceed {self.max_brightness}")
        self.brightness = brightness_level

    def set_color(self, color: str, position: Position) -> None:
        if not position in self.brightness_color_paths:
            raise RuntimeError(f"{position} is not supported for model {self.laptop_model}")
        write_file(self.brightness_color_paths[position], color)

    @property
    def brightness(self) -> int:
        return int(read_file(path=self.brightness_path))

    @brightness.setter
    def brightness(self, value: int):
        write_file(path=self.brightness_path, value=str(value))

    @property
    def max_brightness(self):
        return int(read_file(path=self.max_brightness_path))

    def _ramp_up(self):
        current_brightness = self._read_brightness()
        while current_brightness < self.brightness_max_value:
            self._set_brightness(value=current_brightness)
            current_brightness += 1

    def _ramp_down(self):
        current_brightness = self._read_brightness()
        while current_brightness > self.brightness_min_value:
            self._set_brightness(value=current_brightness)
            current_brightness -= 1

    def update_color(self, color):
        write_file(path=self.brightness_color, value=color)

    def is_multi_region_color(self) -> bool:
        return len(self.brightness_color_paths) > 1
