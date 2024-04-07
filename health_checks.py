import os
import sys
import shutil
import socket
import psutil
import time
import platform
import subprocess


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


def check_no_network():
    """Returns True if it fails to resolve Google's URL or False if it fails"""
    dns_attempts = 2
    for _ in range(dns_attempts):
        try:
            socket.gethostbyname("www.gmail.com")
            return False
        # TODO #1
        except socket.gaierror:
            time.sleep(1)

    if platform.system() == "Windows":
        cmd = "ping -n 1 8.8.8.8 > NUL 2>&1"
    else:
        cmd = "ping -c 1 8.8.8.8 > /dev/null 2>&1"
    # A 0 means the ping successfully pinged
    return subprocess(cmd, shell=True) != 0


def main():
    checks = [
        (check_reboot, "Pending Reboot"),
        (check_cpu_contrainer, "CPU load to high."),
        (check_root_full, "Root Partition fill"),
        (check_no_network, "No working network"),
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False
    if everything_ok:
        print("Everything is okay")
    if not everything_ok:
        sys.exit(1)


main()
