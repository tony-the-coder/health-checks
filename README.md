Base code for Linux was taken from Google's IT Automation with Python. It only had a few items that were being checked. Everything else is mine. 

Windows and Linux both have a version of a task manager. This is not meant to replace but to supplment the existing task manager and to add information into one location without having to switch tabs.

Checks the health of a computer by looking at

- If Root Directory is full
- If the CPU is running over 75%
- Check if the Disk is full
- Check the Network Connection

Currently being improved so that the script would work on both Windows and Linux system.

Future updates would be to display the information from each check. For example,

- Displaying the current CPU percentage,
- how much storage is in use and how much is available,
- network speed,
- continiously run to send an alert if any of the constraints are seen
- Creating a gui for whole program.
