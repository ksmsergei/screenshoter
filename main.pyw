import pyautogui
import keyboard
import win32process, win32gui
import psutil
from datetime import datetime
from os import makedirs, path


#Name of the key to be pressed
KEY = "print_screen"

#Path to the folder of saved screenshots. Leave empty to save screenshot to the same folder
SCREENSHOTS_FOLDER = "C:/Users/Сергей/Pictures/Screenshots/"

while True:
    #Wait for screenshot key
    keyboard.wait(KEY)

    #Get active process name
    window = win32gui.GetForegroundWindow()
    _, pid = win32process.GetWindowThreadProcessId(window)
    pid_name = psutil.Process(pid).name().rsplit('.', 1)[0]

    #If active procces is "explorer", then it's the desktop
    if pid_name == "explorer":
        pid_name = "Desktop"

    #Create screenshots folder if not exists
    if (not path.exists(SCREENSHOTS_FOLDER + pid_name)):
        makedirs(SCREENSHOTS_FOLDER + pid_name)

    #Generate file name for screenshot
    e = datetime.now()
    screenshot_name = SCREENSHOTS_FOLDER + "/" + pid_name + "/" + pid_name + "_" + e.strftime("%d.%m.%Y_%H-%M-%S.%f")[:-3] + ".png"

    #Take and save screenshot
    img = pyautogui.screenshot()
    img.save(screenshot_name)