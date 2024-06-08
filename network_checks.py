import requests
import speedtest as st


def check_connectivity(url="https://www.google.com", timeout=5):
    """Checks connection using a GET request instead of a ping for better testing"""
    try:
        response = requests.get(url, timeout=timeout)
        print(url, ": responded with status code", response.status_code)
        return True
    except requests.ConnectionError:
        return False


def get_speed_results():
    """Checking the connection speed using speedtest and will return a dictionary of the output"""
    try:
        test = st.Speedtest()
        test.download()
        test.upload()
        results_dict = test.results.dict()
        print("Download Speed:", round(results_dict["download"] / 1000000), "Mbps")
        print("Upload Speed:", round(results_dict["upload"] / 1000000), "Mbps")
        print("Ping:", results_dict["ping"], "ms")
        return results_dict
    except Exception as e:
        print(f"Error performing speed test: {e}")
        return {}
