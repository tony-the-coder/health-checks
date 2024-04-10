import speedtest as st
import subprocess
import platform


def check_no_network():
    """Returns True if network checks faile, False otherwise"""

    if platform.system() == "Windows":
        cmd = "ping -n 1 8.8.8.8 > NUL 2>&1"
        result = subprocess.call(cmd, shell=True)
    else:
        cmd = "ping -c 1 8.8.8.8 > /dev/null 2>&1"
        result = subprocess.call(cmd, shell=True)

    return result != 0


def check_speed():

    test = st.Speedtest()
    test.download()
    test.upload()
    results_dict = test.results.dict()
    print("Download Speed:", round(results_dict["download"] / 1000000), "Mbps")
    print("Download Speed:", round(results_dict["upload"] / 1000000), "Mbps")
    print("Ping:", results_dict["ping"], "ms")
