import requests
import speedtest as st
import subprocess
import platform

"""Random network tests outside of the primary script to confirm that the network is working properly and was partially created with the assistance of Gemini Code Assist"""


def check_url_response(url, timeout=5):
    """
    Checks the response of a URL request.

    Args:
        url (str): The URL to test.
        timeout (int, optional): Timeout in seconds (default: 5).

    Returns:
        tuple: (status_code, response_time)
    """
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code, response.elapsed.total_seconds() * 1000
    except requests.exceptions.RequestException as e:
        print(f"Error requesting {url}: {e}")
        return None, None


def main():
    urls_to_test = [
        "https://www.google.com",
        "https://www.amazon.com",
        "https://www.facebook.com",
        # Add more URLs as needed
    ]

    for url in urls_to_test:
        status_code, response_time = check_url_response(url)
        if status_code:
            print(
                f"{url}: Status Code - {status_code}, Response Time - {response_time:.2f} ms"
            )
        else:
            print(f"{url}: Connection Failed")


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


if __name__ == "__main__":
    main()

check_speed()
