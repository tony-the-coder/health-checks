import sys
import network_checks as nc
import check_disks as cd
import system_checks as sc
import utilities as ut
import time
import datetime as dt
import os
import psutil


def main():
    """We start with the time the scan is first initated."""
    start_time = dt.datetime.now()  # Get current datetime
    print("System checks started at ", start_time.strftime("%Y-%m-%d %H:%M:%S"))
    os_output = ut.check_os()
    os_info_string = "".join([str(x) for x in os_output])
    print("The operating system currently be tested: ", os_info_string)

    """Check is an array of tuples where each tuple calls an imported module and prings a message as the tests are run. """
    checks = [
        (cd.check_disk_full, "Checking Disk Space"),
        # (ut.check_os, "Checking Operating System")
        # (sc.check_reboot, "Checking to see if a reboot is required"),
        (nc.net_con, "Checking your connection"),
    ]
    """Set the everything_ok variable to True that changes to False if any of the checks fail. The loop will iterate through the array and run each function which will then reset everything_okay if needed."""
    everything_ok = True
    for check, msg in checks:
        print(msg)

        if check():
            # print(f"Check '{msg}' failed")
            everything_ok = False

    """Verifies the final value of everything_ok and prints a message"""
    # TODO Create try/except for each test to be sure that script does not fail and enable logging with append to get a continiou log
    if everything_ok:

        print("Everything is okay")
    else:
        print(
            "There is an error somewhere please look for it and let me know. Exiting..."
        )
        sys.exit(1)
    endtime = dt.datetime.now()  # Get current datetime
    print("System checks ended at ", endtime.strftime("%Y-%m-%d %H:%M:%S"))


main()
