import unittest
import subprocess
import platform
from health_checks import check_no_network


class TestCheckNoNetwork(unittest.TestCase):

    def test_windows_success(self):
        """Test the check_no_network function on Windows with a successful ping."""
        result = subprocess.call("ping -n 1 8.8.8.8 > NUL 2>&1", shell=True)
        self.assertEqual(check_no_network(), result != 0)

    def test_windows_failure(self):
        """Test the check_no_network function on Windows with a failed ping."""
        result = subprocess.call("ping -n 1 192.0.2.1 > NUL 2>&1", shell=True)
        self.assertEqual(check_no_network(), result != 0)

    def test_linux_success(self):
        """Test the check_no_network function on Linux with a successful ping."""
        result = subprocess.call("ping -c 1 8.8.8.8 > /dev/null 2>&1", shell=True)
        self.assertEqual(check_no_network(), result != 0)

    def test_linux_failure(self):
        """Test the check_no_network function on Linux with a failed ping."""
        result = subprocess.call("ping -c 1 192.0.2.1 > /dev/null 2>&1", shell=True)
        self.assertEqual(check_no_network(), result != 0)


if __name__ == "__main__":
    unittest.main()
