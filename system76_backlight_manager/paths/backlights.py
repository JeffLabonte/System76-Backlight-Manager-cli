from system76_backlight_manager.enums import Position


SINGLE_BACKLIGHT_PATH = {
    "brightness_path": "/sys/class/leds/system76_acpi::kbd_backlight/brightness",
    "brightness_color": {
        Position.CENTER.name: "/sys/class/leds/system76_acpi::kbd_backlight/color",
    },
    "max_brightness_path": "/sys/class/leds/system76_acpi::kbd_backlight/max_brightness",
}


FOUR_BACKLIGHT_PATH = {
    "brightness_path": "/sys/class/leds/system76::kbd_backlight/brightness",
    "brightness_color": {
        Position.LEFT.name: "/sys/class/leds/system76::kbd_backlight/color_left",
        Position.CENTER.name: "/sys/class/leds/system76::kbd_backlight/color_center",
        Position.RIGHT.name: "/sys/class/leds/system76::kbd_backlight/color_right",
        Position.EXTRA.name: "/sys/class/leds/system76::kbd_backlight/color_extra",
    },
    "max_brightness_path": "/sys/class/leds/system76::kbd_backlight/max_brightness",
}


LEGACY_SINGLE_BACKLIGHT_PATH = {
    "brightness_path": "/sys/class/leds/system76::kbd_backlight/brightness",
    "brightness_color": {
        Position.CENTER.name: "/sys/class/leds/system76::kbd_backlight/color_left",
    },
    "max_brightness_path": "/sys/class/leds/system76::kbd_backlight/max_brightness",
}
