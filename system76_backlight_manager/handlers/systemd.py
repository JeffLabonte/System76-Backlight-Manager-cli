import dbus


class SystemdHandler:
    MODE = "fail"

    def __init__(self, unit_name: str):
        self.system_dbus = dbus.SystemBus()
        self.systemd = self.system_dbus.get_object(
            "org.freedesktop.systemd1",
            "/org/freedesktop/systemd1",
        )
        self.manager = dbus.Interface(
            object=self.systemd,
            dbus_interface="org.freedesktop.systemd1.Manager",
        )
        self.unit_name = unit_name

    def get_status(self) -> bool:
        status_str = str(self.manager.GetUnitFileState(self.unit_name))
        return status_str == "enabled"

    def stop_service(self) -> None:
        self.manager.StopUnit(self.unit_name, self.MODE)

    def start_service(self) -> None:
        self.manager.StartUnit(self.unit_name, self.MODE)

    def enable_service(self) -> None:
        pass
