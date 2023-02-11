import pyautogui
import time

print('AutoFishOmegaMC v1.0')

def Fishing():
    print(pyautogui.click(button='right'))
    time.sleep(0.5)
    pyautogui.press('1')
    pyautogui.click(button='right')
    time.sleep(2)
    print('ok')

while True:
    position = pyautogui.locateOnScreen("search.png")
    if bool(position) == True:
        Fishing()
    time.sleep(0.3)
    
    
    
    
    
     
 
     
    
     