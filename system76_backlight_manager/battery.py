from common import read_file


class Battery:
    FULL_BATTERY_PATH = "/sys/class/power_supply/BAT0/charge_full"
    CURRENT_BATTERY_PATH = "/sys/class/power_supply/BAT0/charge_now"

    def _read_current_battery(self) -> int:
        return int(read_file(self.CURRENT_BATTERY_PATH))

    def _read_full_battery(self) -> int:
        return int(read_file(self.FULL_BATTERY_PATH))

    def get_battery_level(self) -> int:
        current = self._read_current_battery()
        full = self._read_full_battery()

        return (current * 100) // full
