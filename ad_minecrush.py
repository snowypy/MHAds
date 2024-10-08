from time import sleep, strftime, localtime, time  # Importing 'time' module
import random
import keyboard
import pyautogui
import threading
import subprocess
import json
import tkinter as tk


class AutoAdBot:
    def __init__(self, config_file):
        self.bot_flag = True
        self.config = self.load_config(config_file)
        self.last_ad_time = None
        self.last_ad_index = None
        self.next_ad_time = None

    def load_config(self, config_file):
        with open(config_file, 'r') as f:
            return json.load(f)

    def run(self):
        print('\nTo end the program: press X for 3 sec')
        print('Starting autoad in 5 sec\n')
        sleep(4)

        try:
            t1 = threading.Thread(target=self.autoad)
            t1.start()

            t2 = threading.Thread(target=self.update_display)
            t2.start()

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
            choice = random.randint(0, len(self.config["messages"]) - 1)
            sleeptime = random.randint(self.config["min_ad_delay"], self.config["max_ad_delay"])

            # Show warning in a new console tab
            print('\nDisplaying warning message\n')
            subprocess.Popen(
                'start cmd /c "echo WARNING: Advertisement will be sent in 3 seconds! Do not touch anything && timeout 3 && echo Closing warning!"',
                shell=True)
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

            message = self.config["messages"][choice]
            pyautogui.typewrite(message)  # Type message
            keyboard.press_and_release('enter')  # Send message
            sleep(1)  # Wait for message to send

            # Update last ad time and index
            self.last_ad_time = strftime('%H:%M:%S', localtime())
            self.last_ad_index = choice

            # Simulate player movement after ad
            self.simulate_movement()

            # Minimize Minecraft
            pyautogui.hotkey('win', 'down')
            pyautogui.hotkey('alt', 'tab')

            # Update next ad time
            self.next_ad_time = strftime('%H:%M:%S', localtime(time() + sleeptime))

            sleep(sleeptime / 1000)

    def simulate_movement(self):
        # Simulate player movement using W, A, S, D keys
        for _ in range(random.randint(2, 3)):  # Move for random number of times
            keyboard.press('w')
            sleep(random.uniform(self.config["min_movement_delay"] / 1000, self.config["max_movement_delay"] / 1000))
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

    def pause_execution(self):
        print('\nPausing execution for 1-3 hours.\n')
        sleep(random.randint(self.config["min_pause_duration"], self.config["max_pause_duration"]) / 1000)

    def update_display(self):
        root = tk.Tk()
        root.title("AutoAd Information")

        last_ad_label = tk.Label(root, text="Last Ad Time: ")
        last_ad_label.grid(row=0, column=0)
        last_ad_info = tk.Label(root, textvariable=self.last_ad_time)
        last_ad_info.grid(row=0, column=1)

        last_ad_index_label = tk.Label(root, text="Last Ad Index: ")
        last_ad_index_label.grid(row=1, column=0)
        last_ad_index_info = tk.Label(root, textvariable=self.last_ad_index)
        last_ad_index_info.grid(row=1, column=1)

        next_ad_label = tk.Label(root, text="Next Ad Time: ")
        next_ad_label.grid(row=2, column=0)
        next_ad_info = tk.Label(root, textvariable=self.next_ad_time)
        next_ad_info.grid(row=2, column=1)

        root.mainloop()


if __name__ == "__main__":
    bot = AutoAdBot("config.json")
    bot.run()
