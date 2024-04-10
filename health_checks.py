import os
import sys
import network_checks as nc
import system_checks as sc


def main():
    checks = [
        (sc.check_reboot, "Pending Reboot"),
        (sc.check_cpu_contrainer, "CPU load to high."),
        (sc.check_root_full, "Root Partition fill"),
        (nc.check_no_network, "No working network"),
        (nc.check_speed, "Checking internet speed not available"),
    ]
    everything_ok = True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok = False
    if everything_ok:
        nc.check_speed()
        print("Everything is okay")
    if not everything_ok:
        sys.exit(1)


main()
