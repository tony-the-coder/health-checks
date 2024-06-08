import shutil


def check_disk_usage(disks=["/"], min_gb=2, min_percent=10):
    """
    Checks disk usage of specified disks or partitions.

    Args:
        disks (list): A list of disks or partitions to check (default: ["/"]).
        min_gb (float): Minimum free space in gigabytes required.
        min_percent (float): Minimum percentage of free space required.

    Returns:
        list: A list of messages indicating disk usage issues, or an empty list if all okay.
    """
    issues = []
    for disk in disks:
        du = shutil.disk_usage(disk)
        percent_free = 100 * du.free / du.total
        gigabytes_free = du.free / 2**30

        # Display free space information
        print(
            f"Disk {disk} has {percent_free:.2f}% free space ({gigabytes_free:.2f} GB available)"
        )

        if gigabytes_free < min_gb:
            issues.append(
                f"Disk {disk} has less than {min_gb:.2f} GB free ({gigabytes_free:.2f} GB available)."
            )
        if percent_free < min_percent:
            issues.append(
                f"Disk {disk} has less than {min_percent:.2f}% free space ({percent_free:.2f}% available)."
            )

    return issues
