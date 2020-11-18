import pyautogui
import cv2 as cv
from time import sleep
from time import time
from windowcapture import WindowCapture
from vision import Vision
from multiprocessing import Process

DELAY_BETWEEN_COMMANDS = 1.00


def main():
    
    initializePyAutoGUI()
    countdownTimer()

   
    
    goToMedBayClick()
    #reportMousePosition()
   

   
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
   

def opencv():
        # initialize the WindowCapture class
    wincap = WindowCapture('BlueStacks')
    # initialize the Vision class
    vision_red_left = Vision('character2.jpg')
    #vision_red_right = Vision('character2.jpg')



    loop_time = time()
    while(True):

        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        # display the processed image
        points = vision_red_left.find(screenshot, 0.9, 'rectangles')
     

        # debug the loop rate
        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

    print('Done.')

def haar():
    wincap = WindowCapture('BlueStacks')

    # load the trained model
    cascade_limestone = cv.CascadeClassifier('among_us.xml')
    # load an empty Vision class
    vision_limestone = Vision(None)

    loop_time = time()
    while(True):

        # get an updated image of the game
        screenshot = wincap.get_screenshot()

        # do object detection
        rectangles = cascade_limestone.detectMultiScale(screenshot,scaleFactor=1.2, 
                                    minNeighbors=5, 
                                    minSize=(24, 24),
                                    flags=cv.CASCADE_SCALE_IMAGE)
        print(vision_limestone.get_click_points(rectangles))

        # draw the detection results onto the original image
        detection_image = vision_limestone.draw_rectangles(screenshot, rectangles)

        # display the images
        cv.imshow('Matches', detection_image)

        # debug the loop rate
        #print('FPS {}'.format(1 / (time() - loop_time)))
        #loop_time = time()

        # press 'q' with the output window focused to exit.
        # press 'f' to save screenshot as a positive image, press 'd' to 
        # save as a negative image.
        # waits 1 ms every loop to process key presses
        key = cv.waitKey(1)
        if key == ord('q'):
            cv.destroyAllWindows()
            break
        elif key == ord('f'):
            cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
        elif key == ord('d'):
            cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)

    print('Done.')

if __name__ == "__main__":
    p1= Process(target = haar)
    p2= Process(target = main)
    p1.start() 
    p2.start()

    p1.join()
    p2.join()
    
