import shutil
import psutil
import platform
import os
import win32api

def check_os():
    """Will return the name of the OS"""
    os_name = platform.system()
    os_version = platform.version()
    print(f"OS: {os_name} {os_version}")
    return os_name, os_version
# check_os()

def check_reboot():
    # Sets the os_name by calling the check_os() function.
    os_name = check_os()
    """Checks for Linux-Specific reboot checks"""

    
    if os_name == "Linux":
        return os.path.exists("/run/reboot-required")
    
        # TODO: #2 Add functionality to check for Windows-Specific reboot checks
        # Windows doumentation on different API calls with direct link to the SM_SUTTINGDOWN information
        # https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-getsystemmetrics#:~:text=SM_SHUTTINGDOWN,is%20not%20supported.
    
    
    elif os_name == "Windows":
        """Checks for Windows-Specific reboot checks"""

        if win32api.GetSystemMetrics(win32api.SM_SHUTTINGDOWN):
            return True
        else:
            return False
    else:
        """Returns a message if the operating system is not supported"""
        return "Operating system not supported"


def check_root_full():
    """Returns True if the Linux root partion is full, False otherwise"""
    os_name = check_os()
    if os_name == "Linux":
        return check_disk_full(disk="/", min_gb=2, min_percent=10)
    elif os_name == "Windows":
        # TODO: #1 Add functionality to check for Windows-Specific root partition checks
        pass
    else:
        """Returns a message if the operating system is not supported"""
        return "Operating system not supported"

def check_cpu_contrainer():
    """True if the cpu is having too much usage, False otherwise"""
    os_name = check_os()
    # Checks for CPU usage on Linux
    if os_name == "Linux":
        return psutil.cpu_percent(1) > 75
    elif os_name == "Windows":
        # TODO: #3 Add functionality to check for Windows-Specific CPU checks
        pass
    else:
        """Returns a message if the operating system is not supported"""
        return "Operating system not supported"


def check_disk_full(disk, min_gb, min_percent):
    """Verifies if the harddrive is full. This part is only a test. Will need to update this"""
    # TODO: Show how much storage is used and how much remains.
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if gigabytes_free < min_gb or percent_free < min_percent:
        return True
    return False
