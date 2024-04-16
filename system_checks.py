import psutil
import platform
import os
import time
import utilities
import win32api
import win32con


def check_reboot():
    """Returns True if the computer has a pending reboot."""

    operating_system_type = utilities.check_os()

    # Checks for reboots on Linux
    if operating_system_type == "Linux":
        return os.path.exists("/run/reboot-required")

    elif operating_system_type == "Windows":
        try:
            key = win32api.RegOpenKeyEx(
                win32con.HKEY_LOCAL_MACHINE,
                "SYSTEM\\CurrentControlSet\\Control\\Session Manager",
                0,
                win32con.KEY_READ,
            )
            value, _ = win32api.RegQueryValueEx(key, "PendingFileRenameOperations")
            if value:
                print("You have a pending reboot")
                return True
            else:
                print("There is no pending reboot")
            return bool(value)
        except FileNotFoundError:
            pass
        print("No pending reboot")
        return False  # No pending reboots

    else:
        print("Reboot not required")
        return False


# TODO  Print out current CPU usage and eventually the highest PID but come up for a good length of time for the snapshot


def check_cpu_contrainer():
    """Verifies which operating system is being used and checks if the CPU is over 75% utilized and will return an error message if the operating system is not supported"""
    operating_system_type = utilities.check_os()
    """Checks if the CPU is over 75% utilized"""
    if operating_system_type == "Linux" or operating_system_type == "Windows":
        return psutil.cpu_percent(1) > 75
    else:
        """Returns a message if the operating system is not supported"""
        return "Operating system not supported"
