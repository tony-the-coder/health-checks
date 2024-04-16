import utilities
import psutil
import os


def check_disk_full(min_gb=2, min_percent=10):
    """Checks if the root partition or a specified disk is full."""

    operating_system = utilities.check_os()

    if operating_system == "Linux":
        disk = "/"
    elif operating_system == "Windows":
        disk = os.environ.get("SystemDrive", "C:")
    else:
        return "Operating system not supported"

    disk_usage = psutil.disk_usage(disk)
    free_bytes_to_gb = disk_usage.free / (1024 * 1024 * 1024)

    print(
        f"Drive {disk} is {disk_usage.percent}% full, with {free_bytes_to_gb:.2f} GB free."
    )
    if (
        disk_usage.free < (min_gb * 1024 * 1024 * 1024)
        or disk_usage.percent < min_percent
    ):
        return True

    return False


# check_disk_full()
