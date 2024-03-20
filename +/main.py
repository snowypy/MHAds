import tkinter as tk
from time import sleep, time, strftime, localtime
import random
import keyboard
import pyautogui
import threading
import subprocess
import json
import tkinter.font as tkFont

class AutoAdBot:
    def __init__(self):
        self.bot_flag = True
        self.pause_flag = False
        self.last_ad_time = 0
        self.load_config()
        self.current_ad_index = 0

        # Initialize Tkinter
        self.root = tk.Tk()
        self.root.title("AutoAd Bot")
        self.root.geometry("400x200")  # Set window size
        self.root.configure(bg="#2C3E50")  # Set background color

        bold_font = tkFont.Font(family="Arial", size=12, weight="bold")

        self.ad_label = tk.Label(self.root, text="Current Ad: ", font=bold_font, fg="#7289DA", bg="#2C3E50")
        self.ad_label.pack(pady=5)

        self.next_ad_frame = tk.Frame(self.root, bg="#23272A")
        self.next_ad_frame.pack(pady=5)
        self.next_ad_label = tk.Label(self.next_ad_frame, text="Next Ad:", font=("Arial", 10), fg="#7289DA", bg="#23272A")
        self.next_ad_label.pack(side=tk.LEFT, padx=5)
        self.next_ad_text = tk.Label(self.next_ad_frame, text="", font=("Arial", 10), fg="#99AAB5", bg="#23272A")
        self.next_ad_text.pack(side=tk.LEFT)

        self.time_until_next_ad_frame = tk.Frame(self.root, bg="#23272A")
        self.time_until_next_ad_frame.pack(pady=5)
        self.time_until_next_ad_label = tk.Label(self.time_until_next_ad_frame, text="Time Until Next Ad:", font=("Arial", 10), fg="#7289DA", bg="#23272A")
        self.time_until_next_ad_label.pack(side=tk.LEFT, padx=5)
        self.time_until_next_ad_text = tk.Label(self.time_until_next_ad_frame, text="", font=("Arial", 10), fg="#99AAB5", bg="#23272A")
        self.time_until_next_ad_text.pack(side=tk.LEFT)


        self.last_ad_frame = tk.Frame(self.root, bg="#23272A")
        self.last_ad_frame.pack(pady=5)
        self.last_ad_label = tk.Label(self.last_ad_frame, text="Last Ad:", font=("Arial", 10), fg="#7289DA", bg="#23272A")
        self.last_ad_label.pack(side=tk.LEFT, padx=5)
        self.last_ad_time_label = tk.Label(self.last_ad_frame, text="", font=("Arial", 10), fg="#99AAB5", bg="#23272A")
        self.last_ad_time_label.pack(side=tk.LEFT)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_ad, font=("Arial", 12), fg="white", bg="#3498DB")
        self.pause_button.pack(pady=5)
        self.unpause_button = tk.Button(self.root, text="Unpause", command=self.unpause_ad, state=tk.DISABLED, font=("Arial", 12), fg="white", bg="#27AE60")
        self.unpause_button.pack(pady=5)

        self.root.after(100, self.autoad_thread)

        self.root.mainloop()

    def load_config(self):
        with open('config.json', encoding='utf-8') as f:
            config = json.load(f)
            self.minecraft_client_name = config.get('minecraft_client_name', 'Lunar Client 1.20.2 (v2.14.5-2411)')
            self.cooldown_min = config.get('cooldown_min', 120)
            self.cooldown_max = config.get('cooldown_max', 240)
            self.pause_min = config.get('pause_min', 3600)
            self.pause_max = config.get('pause_max', 10800)
            self.warning_delay = config.get('warning_delay', 5)
            self.ads = config.get('ads', [])

    def run(self):
        print('\nTo end the program: press X for 3 sec')
        print('Starting autoad in 5 sec\n')
        sleep(4)

    def autoad_thread(self):
        t1 = threading.Thread(target=self.autoad)
        t1.start()

    def open_minecraft(self):
        print('\nOpening Minecraft\n')
        minecraft_window = pyautogui.getWindowsWithTitle(self.minecraft_client_name)
        if minecraft_window:
            minecraft = minecraft_window[0]
            minecraft.restore()
            sleep(0.3)  
            minecraft.maximize()
            try:
                minecraft.activate()  
            except Exception as e:
                print('Error activating Minecraft:', e)
        else:
            print('\nMinecraft is not active')

    def minimize_minecraft(self):
        print('\nMinimizing Minecraft\n')
        minecraft_window = pyautogui.getWindowsWithTitle(self.minecraft_client_name)
        if minecraft_window:
            minecraft = minecraft_window[0]
            minecraft.minimize()
        else:
            print('\nMinecraft is not active')

    def show_warning(self):
        print('\nDisplaying warning message\n')
        subprocess.Popen(f'start cmd /c "echo WARNING: Advertisement will be sent in {self.warning_delay} seconds! && timeout {self.warning_delay} && echo Closing warning!"', shell=True)
        
    def autoad(self):
        print('\nStarting autoad in 2 sec\n')
        sleep(2)
        while self.bot_flag:
            if not self.pause_flag:
                choice = random.randint(1, len(self.ads))
                sleeptime = random.randint(self.cooldown_min, self.cooldown_max)

                self.show_warning()
                sleep(self.warning_delay)  

                self.open_minecraft()

                keyboard.press('esc')
                keyboard.release('esc')
                sleep(0.5) 

                keyboard.press('t')  
                keyboard.release('t')
                sleep(0.5)  

                self.next_ad_text.config(text=self.ads[choice - 1])

                pyautogui.typewrite(self.ads[choice - 1])  
                keyboard.press_and_release('enter')  
                sleep(1) 

                self.last_ad_time = time()

                self.simulate_movement()
                self.minimize_minecraft()

                sleep(sleeptime)

                self.update_info_labels()

    def update_info_labels(self):
        current_time = time()
        next_ad_time = self.last_ad_time + random.randint(self.cooldown_min, self.cooldown_max)
        time_until_next_ad = max(0, next_ad_time - current_time)
        last_ad_str = strftime("%Y-%m-%d %H:%M:%S", localtime(self.last_ad_time))
        next_ad_str = strftime("%Y-%m-%d %H:%M:%S", localtime(next_ad_time))

        # Update Last Ad and Time Until Next Ad labels
        self.last_ad_time_label.config(text=last_ad_str)
        self.time_until_next_ad_text.config(text=f"{next_ad_str}")

    def simulate_movement(self):
        # Simulate player movement using W, A, S, D keys
        choice = random.randint(1, 2)
        for _ in range(random.randint(5, 12)):  # Move for random number of times
            if choice == 1:
                keyboard.press('w')
            if choice == 2:
                keyboard.press('s')
            direction = random.choice(['a', 'd', 'SPACE'])
            keyboard.press(direction)
            sleep(random.uniform(0.1, 0.5))  # Random duration for key press
            keyboard.release(direction)
            if choice == 1:
                keyboard.release('w')
            if choice == 2:
                keyboard.release('s')

    def pause_ad(self):
        self.pause_flag = True
        self.pause_button.config(state=tk.DISABLED)
        self.unpause_button.config(state=tk.NORMAL)

    def unpause_ad(self):
        self.pause_flag = False
        self.pause_button.config(state=tk.NORMAL)
        self.unpause_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    bot = AutoAdBot()
    bot.run()