import pyautogui 
import time
import keyboard

def gc():
        if pyautogui.locateOnScreen(r"/home/tempus/lab/Map-py/t2/gc.png",confidence=0.0) != None:
                caamp_google = pyautogui.locateOnScreen(r"/home/tempus/lab/Map-py/t2/gc.png",confidence=0.0)
                pyautogui.center(caamp_google)
                time.sleep(5)
                pyautogui.write("https://www.youtube.com/@ZackCherry/videos")
                pyautogui.press("enter")
                time.sleep(2)
def sb():
        if pyautogui.locateOnScreen(r"/home/tempus/lab/Map-py/t2/sb.png",confidence=0.9) != None:
                subS = pyautogui.locateOnScreen(r"/home/tempus/lab/Map-py/t2/sb.png",confidence=0.9)
                pyautogui.center(subS)
                time.sleep(5)
                pyautogui.moveTo(subS)
                pyautogui.click()
                time.sleep(2)

response = pyautogui.confirm("Doriti sa incepeti rularea programului","Confirmare")
if(response == "OK"):
        gc()
        sb()
else:
        pyautogui.alert("Ati ales anulare","Anulare")