import cv2 as cv
import numpy as np
import os
import pyautogui
from time import sleep

DELAY_BETWEEN_COMMANDS = 1.00
os.chdir(os.path.dirname(os.path.abspath(__file__)))



def main():
    
    initializePyAutoGUI()
    countdownTimer()

   
    
    goToMedBayClick()
    #reportMousePosition()
    haystack_img = cv.imread('albion_farm.jpg', cv.IMREAD_UNCHANGED)
    result = cv.matchTemplate(haystack_img, cv.TM_CCOEFF_NORMED)

   
    print("Done")


def initializePyAutoGUI():
    pyautogui.FAILSAFE = True


def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 10):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")


def holdKey(key, seconds=1.00):
    pyautogui.keyDown(key)
    sleep(seconds)
    pyautogui.keyUp(key)
    sleep(DELAY_BETWEEN_COMMANDS)


def reportMousePosition(seconds=10):
    for i in range(0, seconds):
        print(pyautogui.position())
        sleep(1)


def goToMedBay():
 
    # Face the entrance
    holdKey('a', 3.)
    holdKey('w', 0.4)
    holdKey('a', 1)
    holdKey('s', 3)


def goToMedBayClick():
    pyautogui.mouseDown(button='left', x=262, y=366)
    sleep(2.00)
    pyautogui.mouseUp(button='left')
    pyautogui.mouseDown(button='left', x=630, y=317)
    sleep(0.4)
    pyautogui.mouseUp(button='left')
    pyautogui.mouseDown(button='left', x=550, y=410)
    sleep(1.2)
    pyautogui.mouseUp(button='left')
    pyautogui.mouseDown(button='left', x=593, y=636)
  
    sleep(2)
    pyautogui.mouseUp(button='left')
   



if __name__ == "__main__":
    main()
