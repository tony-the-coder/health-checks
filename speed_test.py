import network_checks as nc
import system_checks as sc
import platform
import subprocess


# Function to check connecetivity
def check_no_network():
    """Returns True if network checks faile, False otherwise"""

    if platform.system() == "Windows":
        cmd = "ping -n 1 8.8.8.8 > NUL 2>&1"
        result = subprocess.call(cmd, shell=True)
    else:
        cmd = "ping -c 1 8.8.8.8 > /dev/null 2>&1"
        result = subprocess.call(cmd, shell=True)

    return result != 0


print(check_no_network)
