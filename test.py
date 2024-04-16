import win32con

attributes = dir(win32con)
if "SM_SHUTDOWN" in attributes:
    print("FOUND IT")
else:
    print("Not found")
