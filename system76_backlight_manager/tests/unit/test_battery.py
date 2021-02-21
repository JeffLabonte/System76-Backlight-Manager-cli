from unittest.mock import patch

from system76_backlight_manager.battery import Battery

import pytest

FULL_BATTERY_VALUE = 6345000


@pytest.mark.parametrize(
    "current_battery, expected_level",
    [
        (
            FULL_BATTERY_VALUE,
            100,
        ),
        (
            5570000,
            87,
        ),
        (
            3000000,
            47,
        ),
    ],
)
def test_battery__get_battery_level__should_return_batteru_level(
    current_battery,
    expected_level,
):
    with patch.object(Battery, "_read_current_battery", return_value=current_battery) as current_battery, patch.object(
        Battery, "_read_full_battery", return_value=FULL_BATTERY_VALUE
    ) as full_battery_mock:

        battery = Battery()
        assert battery.get_battery_level() == expected_level

        current_battery.assert_called_once()
        full_battery_mock.assert_called_once()
