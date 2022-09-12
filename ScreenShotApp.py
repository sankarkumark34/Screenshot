import time 
import pyautogui

def screenshot():
    name =int(round(time.time()*1000))
    name= 'F:/projects/Python/ScreenShot/{}.jpg'.format(name)
    time.sleep(2.5)
    img =pyautogui.screenshot(name)
    img.show()

screenshot()
