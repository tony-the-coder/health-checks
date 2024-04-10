import shutil
import psutil
import platform
import os


def check_reboot():
    """Returns True if the computer has a pending reboot"""

    if platform.system() == "Linux":
        return os.path.exists("/run/reboot-required")
    elif platform.system() == "Windows":
        # TODO: #2 Add functionality to check for Windows-Specific reboot checks
        pass
    else:
        # Checks for reboots on other OS, but I am thinking that this is just a clean way to exit.
        return False


def check_root_full():
    """Returns True if the root partion is full, False otherwise"""
    return check_disk_full(disk="/", min_gb=2, min_percent=10)


def check_cpu_contrainer():
    """True if the cpu is having too much usage, False otherwise"""
    return psutil.cpu_percent(1) > 75


def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False
