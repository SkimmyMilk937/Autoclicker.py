"""Written by Nicolas Attefat
12/18/23
Autoclicker application in python
autoclicker.py
"""

from time import sleep
from sys import exit
from keyboard import add_hotkey
from keyboard import wait
import pyautogui

def welcome():
    intro = pyautogui.confirm("Wellcom to autoclicker.py", "autoclicker.py", buttons=["exit", "proceed"])
    
    if (intro == "exit"):
        exit()
    else:
        inTime()
        pyautogui.alert("autoclicker operational - press: [" + hotkey + "] to activate", "autoclicker.py" )

def inTime():
    global speed
    speed = pyautogui.prompt("AUTOCLICKER SPEED (how many seconds to delay each click)", "autoclicker.py")
    
    if(speed != None):
        try:
            (float(speed))
        except:
            pyautogui.alert("Not a valid value", "autoclicker.py")
            inTime()
            
    speed = (float(speed))
    
    global hotkey
    hotkey = pyautogui.prompt("Now enter desired \'hot-key\' for activating/disabling autoclicker (exe. [ctrl+alt])", "autoclicker.py")
    add_hotkey(hotkey, lambda: click())

    
def click():
    global enabled
    if enabled == False:
        enabled = True
    else:
        enabled = False

if __name__ == '__main__':
    global enabled
    enabled = False
    
    welcome()
    
    while True:
        wait(hotkey)
        while enabled:
            pyautogui.click() 
            sleep(speed)
