from unittest.mock import patch

from system76_backlight_manager.keyboard_backlight import KeyboardBacklight

import pytest


def setup_keyboard_backlight(laptop_model: str) -> KeyboardBacklight:
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
