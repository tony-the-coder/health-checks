# import psutil
# import os
# import time
# import win32api
# import win32con
"""A bunch of failed testing that I can can go back and review later. to learn where I went wrong"""
# def check_windows_root_full(min_gb=2, min_percent=10):
#     """Returns True if the Windows root partition is full, False otherwise."""

#     root_drive = os.environ.get("SystemDrive", "C:")  # Get root drive (usually "C:")
#     print(root_drive)
#     disk_usage = psutil.disk_usage(root_drive)

#     # Check if free space is below either threshold
#     if disk_usage.free < (min_gb * 1024 * 1024 * 1024):  # Check in GB
#         return True
#     if disk_usage.percent < min_percent:
#         return True
#     print(disk_usage.free)
#     return False  # Not full


# print(check_windows_root_full())


# def check_cpu_constrainer():
#     """Returns True if the CPU is having too much usage, False otherwise"""
#     psutil.cpu_percent()  # Take initial snapshot
#     time.sleep(30)  # Wait a short period
#     cpu_usage = psutil.cpu_percent()
#     print(cpu_usage)
#     return cpu_usage > 75


# check_cpu_constrainer()
# def check_speed():

#     test = st.Speedtest()
#     test.download()
#     test.upload()
#     results_dict = test.results.dict()
#     return results_dict

# import psutil

# boot_time = psutil.boot_time()
# current_time = time.time()
# shutdown_threshold = 60  # Detect shutdowns within the last minute

# if current_time - boot_time < shutdown_threshold:
#     print("Shutdown detected within the last minute")
#     return True
# else:
#     print("No recent shutdown detected")
#     return False
