import dbus


class SystemdHandler:
    def __init__(self, unit_name):
        self.system_dbus = dbus.SystemBus()
        self.systemd = self.system_dbus.get_object(
            "org.freedesktop.systemd1",
            "/org/freedesktop/systemd1",
        )
        self.manager = dbus.Interface(
            object=self.systemd,
            dbus_interface="org.freedesktop.systemd1.Manager",
        )
