#!/usr/bin/env python3

from tkinter import Tk, Label
from threading import Thread
from time import sleep
import time
import threading
import random
import keyboard
import pyautogui
import subprocess

class AutoAdBot:
    def __init__(self):
        self.bot_flag = True
        self.last_ad_time = None
        self.next_ad_time = None

    def run(self):
        print('\nTo end the program: press X for 3 sec')
        print('Starting autoad in 5 sec\n')
        sleep(4) 

        try:
            t1 = threading.Thread(target=self.autoad) 
            t1.start()

            # Start a timer for 1-3 hours (3600 to 10800 seconds)
            timer_thread = threading.Timer(random.randint(3600, 10800), self.pause_execution)
            timer_thread.start()

            while self.bot_flag:
                sleep(3)
                if keyboard.is_pressed('x'):
                    self.bot_flag = False
                    return   
        except Exception as e:
            print(e)

        print('\nTHAT\'S DONE!!\n')

    def open_minecraft(self):
        print('\nOpening Minecraft\n')
        minecraft_window = pyautogui.getWindowsWithTitle('Lunar Client 1.20.2 (v2.14.5-2411)')
        if minecraft_window:
            minecraft = minecraft_window[0]
            if minecraft.isMinimized:
                print('\nMinecraft is minimized')
                minecraft.restore()
                sleep(1)  # Add a delay to ensure the window becomes active
            minecraft.maximize()
            try:
                minecraft.activate()  # Bring Minecraft to the front
            except Exception as e:
                print('Error activating Minecraft:', e)
        else:
            print('\nMinecraft is not active')

    def autoad(self):
        print('\nStarting autoad in 2 sec\n')
        sleep(2)
        print('\nStarting autoad in NOW\n')
        while self.bot_flag:
    
            choice = random.randint(1, 6)
            sleeptime = random.randint(140, 270)
    
            # Show warning in a new console tab
            print('\nDisplaying warning message\n')
            subprocess.Popen('start cmd /c "color 0C && echo WARNING: Advertisement will be sent in 3 seconds! Do not touch anything && timeout 3 && echo Closing warning!"', shell=True)
            sleep(4)  # Wait for the warning message to be displayed
    
            self.open_minecraft()
            # Close any open GUI
            keyboard.press('esc')  
            keyboard.release('esc')
            sleep(0.5)  # Wait for GUI to close
            
            self.simulate_movement()
            
            keyboard.press('t')  # Open chat
            keyboard.release('t')
            sleep(0.5)  # Wait for chat to open
            messages = [
                '/ad HARDCORE &#FF870F&lHARDEST MINECRAFT SERVER &f&l| &#FF590F&lCAN YOU BEAT HARDCORE??',
                '/ad hardcore &c&lOFFICIAL HARDCORE SERVER &e| &6&lJUST RELEASED! &e| &a[CLICK HERE]',
                '/ad L1FESTEE1 &#e97dfa&lCRYSTAL PVP &r&f| &#fc4cb0&lPOT &8[&d&l&nCLICK HERE&8&l]',
                '/ad L1FESTEE1 &#8cff00&lDUPE &f| &#8cff00&lLIKE DONUTSMP&r&f | &8[&#f74d0a&l&nCLICK&8]',
                '/ad L1FESTEE1 &#fa7d9a&lDUPE &r&f| &#f51448&lCRYSTAL &8[&e&l&nCLICK HERE&8&l]',
                '/ad L1FESTEE1 &#e97dfa&lCRYSTAL PVP &r&f| &#fc4cb0&lDUPE &8[&d&l&nCLICK HERE&8&l]'
                '/ad L1FESTEE1 &#A12AEE&lPUBLIC LIFESTEAL SMP &f&l| &#EE2AEE>&lDUPE BUG &8[&d&l&nCLICK HERE&8&l]'
            ]
            pyautogui.typewrite(messages[choice - 1])  # Type message
            keyboard.press_and_release('enter')  # Send message
            sleep(1)  # Wait for message to send
    
            # Update last advertisement time
            self.last_ad_time = time.strftime("%Y-%m-%d %H:%M:%S")
            update_gui()  # Update GUI after displaying advertisement
    
            # Simulate player movement after ad
            self.simulate_movement()
    
            # Minimize Minecraft
            pyautogui.hotkey('win', 'down')
            pyautogui.hotkey('alt', 'tab')
    
            # Update next advertisement time after scheduling the next advertisement
            next_ad_time = time.time() + random.randint(3600, 10800)
            self.next_ad_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(next_ad_time))
            update_gui()  # Update GUI after scheduling next advertisement
    
            sleep(sleeptime)
            update_gui()

    def simulate_movement(self):
        # Simulate player movement using W, A, S, D keys
        for _ in range(random.randint(1, 2)):  # Move for random number of times
            keyboard.press('w')
            sleep(random.uniform(0.17, 0.41))
            keyboard.press('CTRL')	
            sleep(random.uniform(0.21, 0.41))
            keyboard.press('SPACE')
            sleep(random.uniform(0.1, 0.5))  # Random duration for key press
            direction2 = random.choice(['a', 'd'])
            keyboard.press(direction2)
            keyboard.release('W')
            sleep(random.uniform(0.3, 0.5))
            keyboard.release('CTRL')
            sleep(random.uniform(0.3, 0.5))
            keyboard.release(direction2)
            keyboard.release('SPACE')
            
    
    def move_mouse_in_window(self):
        minecraft_window = pyautogui.getWindowsWithTitle('Lunar Client 1.20.2 (v2.14.5-2411)')
        if minecraft_window:
            minecraft = minecraft_window[0]
            x, y, _, _ = minecraft.box
            new_x = random.randint(x, x + minecraft.width)
            new_y = random.randint(y, y + minecraft.height)
            pyautogui.moveTo(new_x, new_y, duration=0.1)

    def pause_execution(self):
        print('\nPausing execution for 1-3 hours.\n')
        sleep(random.randint(5600, 10800))  # Pause for 1-3 hours (3600 to 10800 seconds)

def update_gui():
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    last_ad_time_label.config(text=f"Last Advertisement: {bot.last_ad_time}")
    next_ad_time_label.config(text=f"Next Advertisement: {bot.next_ad_time}")

    # Calculate the remaining time until the next advertisement
    if bot.next_ad_time:
        next_ad_time = time.strptime(bot.next_ad_time, "%Y-%m-%d %H:%M:%S")
        current_time = time.strptime(current_time, "%Y-%m-%d %H:%M:%S")
        remaining_time = time.mktime(next_ad_time) - time.mktime(current_time)
        remaining_time_str = time.strftime("%H:%M:%S", time.gmtime(remaining_time))
        remaining_time_label.config(text=f"Time Until Next Ad: {remaining_time_str}")
    else:
        remaining_time_label.config(text="Time Until Next Ad: Not scheduled yet")

    root.after(1000, update_gui)

if __name__ == "__main__":
    bot = AutoAdBot()

    # Setup GUI
    root = Tk()
    root.title("Auto Ad Bot Information")
    root.geometry("400x250")

    last_ad_time_label = Label(root, text="Last Advertisement: Not yet displayed")
    last_ad_time_label.pack()

    next_ad_time_label = Label(root, text="Next Advertisement: Not yet scheduled")
    next_ad_time_label.pack()

    remaining_time_label = Label(root, text="Time Until Next Ad: Not scheduled yet")
    remaining_time_label.pack()

    # Start GUI update
    update_gui()

    # Start autoad function in a separate thread
    t = Thread(target=bot.run)
    t.start()

    root.mainloop()
