#!python
import time
import pyautogui
import pygetwindow as gw
from os import system
import os
os.system('title sql')
import subprocess
if __name__ =="__main__":
    folder_path = "VS CODE PATH"
    subprocess.Popen([folder_path]) 
    time.sleep(1)
    terminal_window = None
    while terminal_window is None:
        terminal_window = gw.getWindowsWithTitle("sql")[0]
    terminal_window.minimize()
    vs_window = None
    while vs_window is None:
        vs_window = gw.getWindowsWithTitle('Visual Studio Code')[0]
    # Maximize the Visual Studio window
    vs_window.maximize()
    time.sleep(1)
    while True:
        try:
            pyautogui.moveTo(1919,300)
            pyautogui.dragTo(1919,399)
            pyautogui.moveTo(1919,400)
            time.sleep(1)
            if(pyautogui.position().x!=1919  and  pyautogui.position().y!=300 and pyautogui.position().y!=400):
                terminal_window.close()
                
        except KeyboardInterrupt:
             exit()
            
