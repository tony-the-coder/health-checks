# import win32api
# import win32con
# import platform
# import time
# import psutil
# import os


# def check_os():
#     """Will return the name of the OS"""
#     operating_system_type = platform.system()
#     os_version = platform.version()
#     # print(f"OS: {operating_system_type} {os_version}")

#     return operating_system_type


# def check_reboot():
#     """Returns True if the computer has a pending reboot."""

#     operating_system_type = check_os()

#     # Checks for reboots on Linux
#     if operating_system_type == "Linux":
#         return os.path.exists("/run/reboot-required")

#     elif operating_system_type == "Windows":
#         print("Checking for Windows reboot")
#         print("Inside Windows block")
#         print("Calling GetSystemMetrics")

#         shutdown_flag = win32api.GetSystemMetrics(win32con.SM_SHUTTINGDOWN)
#         print("Shutdown Flag Value:", shutdown_flag)

#         if shutdown_flag:
#             return True
#         else:
#             return False

#     # If the operating system is not supported
#     else:
#         return "Operating system not supported"


# def check_reboot():
#     """Returns True if the computer has a pending reboot."""

#     operating_system_type = check_os()

#     # Checks for reboots on Linux
#     if operating_system_type == "Linux":
#         return os.path.exists("/run/reboot-required")

#     elif operating_system_type == "Windows":
#         import psutil

#         boot_time = psutil.boot_time()
#         current_time = time.time()
#         shutdown_threshold = 60  # Detect shutdowns within the last minute

#         if current_time - boot_time < shutdown_threshold:
#             print("Shutdown detected within the last minute")
#             return True
#         else:
#             print("No recent shutdown detected")
#             return False


# check_reboot()


# def check_no_network():
#     """Returns True if network checks faile, False otherwise"""

#     if platform.system() == "Windows":
#         cmd = "ping -n 1 8.8.8.8 > NUL 2>&1"
#         result = subprocess.call(cmd, shell=True)
#     else:
#         cmd = "ping -c 1 8.8.8.8 > /dev/null 2>&1"
#         result = subprocess.call(cmd, shell=True)


# def check_speed():

#     # Get the JSON output from the speedtest-cli command
#     json_output = subprocess.check_output(["speedtest-cli", "--json"])

#     # Parse the JSON output
#     results_dict = json.loads(json_output)

#     # Print the results
#     print("Download Speed:", round(results_dict["download"] / 1000000), "Mbps")
#     print("Upload Speed:", round(results_dict["upload"] / 1000000), "Mbps")
#     print("Ping:", results_dict["ping"], "ms")
# import speedtest as st
# import subprocess
# import platform


# def check_no_network():
#     """Returns True if network checks faile, False otherwise"""

#     if platform.system() == "Windows":
#         cmd = "ping -n 1 8.8.8.8 > NUL 2>&1"
#         result = subprocess.call(cmd, shell=True)
#     else:
#         cmd = "ping -c 1 8.8.8.8 > /dev/null 2>&1"
#         result = subprocess.call(cmd, shell=True)

#     return result != 0


# def check_speed():

#     test = st.Speedtest()
#     test.download()
#     test.upload()
#     results_dict = test.results.dict()
#     print("Download Speed:", round(results_dict["download"] / 1000000), "Mbps")
#     print("Download Speed:", round(results_dict["upload"] / 1000000), "Mbps")
#     print("Ping:", results_dict["ping"], "ms")


# check_no_network()
# check_speed()

# Function to check connecetivity
# def check_no_network():
#     """Returns True if network checks faile, False otherwise"""

#     if platform.system() == "Windows":
#         cmd = "ping -n 1 8.8.8.8 > NUL 2>&1"
#         result = subprocess.call(cmd, shell=True)
#     else:
#         cmd = "ping -c 1 8.8.8.8 > /dev/null 2>&1"
#         result = subprocess.call(cmd, shell=True)

#     return result != 0


# def check_speed():

#     test = st.Speedtest()
#     test.download()
#     test.upload()
#     results_dict = test.results.dict()
#     print("Download Speed:", round(results_dict["download"] / 1000000), "Mbps")
#     print("Download Speed:", round(results_dict["upload"] / 1000000), "Mbps")
#     print("Ping:", results_dict["ping"], "ms")


"""This was one of my several (somewhat failed ideas) to get the information. It took a while because the speedtest-cli would only work on certain environments and for some reason I could not switch them. I will be keeping this for posterity to help me in the future and give me something I cold possibly improve in the future. """
# def run_speedtest():
#     """Executes speedtest-cli and prints the output"""
#     result = subprocess.run(["speedtest-cli", "--json"], stdout=subprocess.PIPE)
#     output = result.stdout.decode("utf-8")
#     print(output)


# if __name__ == "__main__":
#     if check_connection():  # Directly use the result of check_connection()
#         print("internet connection found..")
#         run_speedtest()
#     else:
#         print("no Internet connection found.")

#     print("Done.")
"""Part of my almost final script with lots of debugging print statements also keeping this to refer to as reminders"""


# def check_speed():

#     test = st.Speedtest()
#     test.download()
#     test.upload()
#     results_dict = test.results.dict()
#     # # print("Server:", results_dict["server"]["name"])  # Server name
#     # # print(
#     # #     "Latency:", results_dict["server"]["latency"], "ms"
#     # # )  # Checks the latency of the connections
#     # # print(
#     # #     "Download Speed:", round(results_dict["download"] / 1000000), "Mbps"
#     # # )  # Checks the download speed in bits and turns to Mbps
#     # # print(
#     # #     "Upload Speed:", round(results_dict["upload"] / 1000000), "Mbps"
#     # # )  # Checks the upload speed in bits and turns to Mbps
#     # # print("Ping:", results_dict["ping"], "ms")
#     # return results_dict


# print("Checking Internet Connection...")  # Just in case I need to debug.


# if check_connection():
#     print("internet connection found..")
#     # speed_results = check_speed()  # Storing the data for print debuging
#     # print(speed_results)  # Verifying the data output
#     check_speed()
# else:
#     print("no Internet connection found.")
# print("Done.")


# def check_connection():
#     """Performs a simple network connectivity check using ping.

#     Returns:
#         True if the ping fails, indicating no connection, False otherwise.
#     """

#     result = subprocess.run(
#         ["ping", "-c", "1", "8.8.8.8"],
#         stdout=subprocess.DEVNULL,
#         stderr=subprocess.DEVNULL,
#     )
#     print("Ping Return Code:", result.returncode)  # For debugging purposes so I do not go mad again
#     return result.returncode != 0


"""This one was more difficult than I thought. I had to do a lot more research because I kept getting stuck in the script somehow. Had to get help"""


# def check_linux_root_full():
#     if check_os == "Linux":
#         return check_disk_full(disk="/", min_gb=2, min_percent=10)
#     else:
#         pass

# def check_windows_root_full(min_gb=2, min_percent=10):
#     """Returns True if the Windows root drive is full, False otherwise"""

#     if check_os() == "Windows":
#         return check_disk_full(disk="C:", min_gb=min_gb, min_percent=min_percent)
#     else:
#         pass
#     root_drive = os.environ.get("SystemDrive", "C:")
#     disk_usage = psutil.disk_usage(root_drive)

#     # Check if free space is below either threshold
#     if disk_usage.free < (min_gb * 1024 * 1024 * 1024):  # Check in GB
#         return True
#     if disk_usage.percent < min_percent:
#         return True
#     return False  # Not full
