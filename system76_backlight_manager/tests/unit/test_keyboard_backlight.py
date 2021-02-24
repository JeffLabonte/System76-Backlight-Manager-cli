from unittest.mock import patch

from system76_backlight_manager.enums import Position
from system76_backlight_manager.keyboard_backlight import KeyboardBacklight

import pytest


def setup_keyboard_backlight(laptop_model: str = "oryp6") -> KeyboardBacklight:
    with patch(
        "system76_backlight_manager.keyboard_backlight.get_laptop_model",
        return_value=laptop_model,
    ):
        return KeyboardBacklight()


@pytest.mark.parametrize(
    "valid_model, number_of_region",
    [
        (
            "oryp6",
            1,
        ),
        (
            "oryp4",
            4,
        ),
        (
            "serw11",
            4,
        ),
    ],
)
def test_keyboard_backlight__init_valid_model__should_not_raise(
    valid_model: str,
    number_of_region: int,
):
    keyboard_backlight = setup_keyboard_backlight(laptop_model=valid_model)
    assert len(keyboard_backlight.brightness_color_paths) == number_of_region


def test_keyboard_backlight__init_invalid_model__should_raise_exception():
    invalid_model = "oryp11"
    with pytest.raises(
        RuntimeError,
        match=f"{invalid_model} is not supported by this script",
    ):
        setup_keyboard_backlight(laptop_model=invalid_model)


def test_keyboard_backlight__breathe__should_call_ramp_up_ramp_down():
    with patch.object(KeyboardBacklight, "_ramp_up",) as ramp_up_mock, patch.object(
        KeyboardBacklight,
        "_ramp_down",
    ) as ramp_down_mock:
        kb = setup_keyboard_backlight()
        kb.breathe()

        ramp_up_mock.assert_called_once()
        ramp_down_mock.assert_called_once()


def test_keyboard_backlight__static___should_call_read_file_and_write():
    with patch(
        "system76_backlight_manager.keyboard_backlight.read_file",
        return_value=255,
    ) as read_file_mock, patch("system76_backlight_manager.keyboard_backlight.write_file") as write_file_mock:
        kb = setup_keyboard_backlight()
        kb.static(brightness_level=255)

        read_file_mock.assert_called_once()
        write_file_mock.assert_called_once()


@pytest.mark.parametrize(
    "laptop_model, position, expected_path, color",
    [
        (
            "darp5",
            Position.CENTER,
            "/sys/class/leds/system76::kbd_backlight/color_left",
            "FFFFFF",
        ),
        (
            "oryp6",
            Position.CENTER,
            "/sys/class/leds/system76_acpi::kbd_backlight/color",
            "FFFFFF",
        ),
        (
            "oryp4",
            Position.CENTER,
            "/sys/class/leds/system76::kbd_backlight/color_center",
            "FFFFFF",
        ),
        (
            "oryp4",
            Position.LEFT,
            "/sys/class/leds/system76::kbd_backlight/color_left",
            "FFFFFF",
        ),
        (
            "oryp4",
            Position.RIGHT,
            "/sys/class/leds/system76::kbd_backlight/color_right",
            "FFFFFF",
        ),
        (
            "oryp4",
            Position.EXTRA,
            "/sys/class/leds/system76::kbd_backlight/color_extra",
            "FFFFFF",
        ),
        (
            "serw11",
            Position.CENTER,
            "/sys/class/leds/system76::kbd_backlight/color_center",
            "FFFFFF",
        ),
        (
            "serw11",
            Position.LEFT,
            "/sys/class/leds/system76::kbd_backlight/color_left",
            "FFFFFF",
        ),
        (
            "serw11",
            Position.RIGHT,
            "/sys/class/leds/system76::kbd_backlight/color_right",
            "FFFFFF",
        ),
        (
            "serw11",
            Position.EXTRA,
            "/sys/class/leds/system76::kbd_backlight/color_extra",
            "FFFFFF",
        ),
        (
            "serw12",
            Position.CENTER,
            "/sys/class/leds/system76::kbd_backlight/color_center",
            "FFFFFF",
        ),
        (
            "serw12",
            Position.LEFT,
            "/sys/class/leds/system76::kbd_backlight/color_left",
            "FFFFFF",
        ),
        (
            "serw12",
            Position.RIGHT,
            "/sys/class/leds/system76::kbd_backlight/color_right",
            "FFFFFF",
        ),
        (
            "serw12",
            Position.EXTRA,
            "/sys/class/leds/system76::kbd_backlight/color_extra",
            "FFFFFF",
        ),
    ],
)
def test_keyboard_backlight__set_color__should_call_write_file_when_position_valid(
    laptop_model,
    position,
    expected_path,
    color,
):
    with patch("system76_backlight_manager.keyboard_backlight.write_file") as write_mock:
        setup_keyboard_backlight(laptop_model=laptop_model).set_color(color, position)
        write_mock.assert_called_once_with(expected_path, color)
