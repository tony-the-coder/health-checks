import subprocess
import speedtest as st
import time
import datetime
import logging


def check_connection():
    # print("***** Inside network_checks.check_connection() *****")
    # print("Checking Internet Connection...")  # Just in case I need to debug.
    """Uses ping to check if there is an internet connection..

    Returns:
        True if the ping fails, indicating no connection, False otherwise.
    """

    result = subprocess.run(
        ["ping", "-c", "1", "8.8.8.8"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("Ping Return Code:", result.returncode)
    # )  # For debugging purposes so I do not go mad again
    print("======================================")
    return result.returncode != 0


def net_con():

    if check_connection():
        print("Connection confirmed...")
        print("Checking Internet Speed...")
        print("======================================")
        check_speed()

    else:
        print("no Internet connection found.")


def check_speed():
    try:
        test = st.Speedtest()
        test.download()
        test.upload()
        results_dict = test.results.dict()
        logging.info("Speed test successful at: %s", datetime.datetime.now())
    except Exception as e:
        print("Error in speedtest:", e)
        logging.error(
            "Speed test failed at: %s with error: %s", datetime.datetime.now(), e
        )
        # return
    print("======================================")
    print("Your download Speed:", round(results_dict["download"] / 1000000), "Mbps")
    print("Your upload Speed:", round(results_dict["upload"] / 1000000), "Mbps")
    print("Ping:", results_dict["ping"], "ms")
    # return results_dict
    # print("Done.")
