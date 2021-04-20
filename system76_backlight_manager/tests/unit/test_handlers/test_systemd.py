from system76_backlight_manager.handlers.systemd import SystemdHandler


def test__systemd__get_status_on_stopped__should_return_false():
    systemd_handler = SystemdHandler(unit_name="sshd.service")
    status = systemd_handler.get_status()

    assert status is False
