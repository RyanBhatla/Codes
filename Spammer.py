#pip install pyautogui and time if needed
#make a document 'script' in the same ide and enter what you want to spam
import pyautogui, time
time.sleep(5)
f = open("script", "r")
for word in f:
    pyautogui.typewrite(word)
    
