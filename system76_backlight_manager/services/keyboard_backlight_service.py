from typing import Dict

from system76_backlight_manager.common import write_file, read_file
from system76_backlight_manager.battery import Battery
from system76_backlight_manager.colors import GREEN, RED, YELLOW
from system76_backlight_manager.keyboard_backlight import KeyboardBacklight
from system76_backlight_manager.enums import Mode


class KeyboardBacklightService(KeyboardBacklight):
    def __init__(self, context: Dict):
        super().__init__()

        self.mode = context.get("mode", Mode.BREATHE)
        self.brightness_max_value = context.get("brightness_max_value", 255)
        self.brightness_min_value = context.get("brightness_min_value", 15)

        self.red_threshold = context.get("red_threshold", 25)
        self.yellow_threshold = context.get("yellow_threshold", 50)

        self.battery_handler = Battery()

    def run(self):
        while True:
            self.mode_functions_mapping[self.mode]()
            self.change_color()

    def change_color(self):
        battery_level = self.battery_handler.get_battery_level()
        if battery_level < self.red_threshold:
            self._set_color(RED)
        elif battery_level < self.yellow_threshold:
            self._set_color(YELLOW)
        else:
            self._set_color(GREEN)

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

    def _set_color(self, color):
        for color_path in self.brightness_color_paths.values():
            write_file(path=color_path, value=color)

    def _set_full_brightness(self):
        write_file(path=self.brightness_path, value=str(self.brightness_max_value))

    def _set_brightness(self, value: int):
        write_file(path=self.brightness_path, value=str(value))

    def _read_brightness(self) -> int:
        return int(read_file(path=self.brightness_path))
