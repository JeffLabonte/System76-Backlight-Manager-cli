from unittest.mock import patch
from typing import Dict

from system76_backlight_manager.services.keyboard_backlight_service import KeyboardBacklightService

import pytest


def setup_keyboard_backlight_service(
    context: Dict = {},
    laptop_model: str = "oryp6",
):
    with patch(
        "system76_backlight_manager.keyboard_backlight.get_laptop_model",
        return_value=laptop_model,
    ):
        kb_service = KeyboardBacklightService(
            context=context,
        )
        assert isinstance(kb_service, KeyboardBacklightService)
        return kb_service


@pytest.mark.parametrize(
    "context, values_expected",
    [
        (
            {},
            {
                "mode": "breathe",
                "brightness_max_value": 255,
                "brightness_min_value": 15,
                "red_threshold": 25,
                "yellow_threshold": 50,
            },
        )
    ],
)
def test_keyboard_backlight_service__init_valid_context__should_not_raise(
    context,
    values_expected,
):
    kb_service = setup_keyboard_backlight_service(context=context)
    for attr, value in values_expected.items():
        assert getattr(kb_service, attr) == value
