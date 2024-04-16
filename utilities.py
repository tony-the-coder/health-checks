import platform


def check_os():
    """Will return the name of the OS and Version of the system"""
    operating_system_type = platform.system()

    return operating_system_type


def dumb_test():
    print("Dumb Test")

    return False
