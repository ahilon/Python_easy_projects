import pyautogui
import time

def searchPicture(name):
        time.sleep(0.5)
        icon = pyautogui.locateOnScreen(str(name), grayscale=True); locateIcon = pyautogui.center(icon)
        print(locateIcon)
        pyautogui.click(locateIcon, duration=0.5)

def savePicture():
        time.sleep(0.2)
        pyautogui.keyDown('ctrlleft'); pyautogui.press('s'); pyautogui.keyUp('ctrlleft')
        time.sleep(0.2)
        pyautogui.typewrite('Labirynt.png')
        searchPicture('save.png')


def openPaint():
        pyautogui.click(190, 1060, duration=0.5); pyautogui.typewrite('paint')
        searchPicture("paint.png")

def drawPicture():
        searchPicture("brush.png")
        pyautogui.moveTo(660,480, duration=0.2)
        distance = 200
        while distance > 0:
                pyautogui.dragRel(distance, 0, duration=0.2)
                distance = distance - 5
                pyautogui.dragRel(0, distance, duration=0.2)
                pyautogui.dragRel(-distance, 0, duration=0.2)
                distance = distance - 5
                pyautogui.dragRel(0, -distance, duration=0.2)




try:

        openPaint()
        drawPicture()
        savePicture()
except KeyboardInterrupt:
        print("Działanie programu zakończone")