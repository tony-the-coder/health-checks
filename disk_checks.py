import os
import pandas as pd
import shared_checks  # Import from shared_checks
from shared_checks import check_disk_usage


def calculate_directory_size(path):
    """Recursively calculates the total size of a directory (in bytes)."""
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                total += calculate_directory_size(entry.path)
            elif entry.is_file(follow_symlinks=False):
                total += entry.stat().st_size
        except PermissionError:
            print(f"Warning: Permission denied for {entry.path}")
        except FileNotFoundError:  # Handle case where a file is deleted during the scan
            print(f"Warning: File not found: {entry.path}")
    return total


def check_directory_size(directory_path):
    """Calculates and displays the size of a specific directory."""
    total_size = calculate_directory_size(directory_path)
    print(f"Total size of directory '{directory_path}': {total_size} bytes")


# check_disk_usage()
