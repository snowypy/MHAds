from time import sleep
import random
import keyboard 
import pyautogui 
import threading
import subprocess

class AutoAdBot:
    def __init__(self):
        self.bot_flag = True

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

    def show_warning(self):
        print('\nDisplaying warning message\n')
        subprocess.Popen(['cmd', '/c', 'echo WARNING: Advertisement will be sent in 3 seconds! && timeout 3 && echo Closing warning!'], shell=True)

    def autoad(self):
        print('\nStarting autoad in 2 sec\n')
        sleep(2)
        while self.bot_flag:
            choice = random.randint(1, 6)
            sleeptime = random.randint(240, 470)

            # Show warning in a new console tab
            self.show_warning()
            sleep(4)  # Wait for the warning message to be displayed

            self.open_minecraft()
            # Close any open GUI
            keyboard.press('esc')  
            keyboard.release('esc')
            sleep(0.5)  # Wait for GUI to close
            
            keyboard.press('t')  # Open chat
            keyboard.release('t')
            sleep(0.5)  # Wait for chat to open
            messages = [
                '/ad KalpeMC &b&lBRAND NEW SERVER NETWORK &f&lCLICK HERE TO JOIN',
                '/ad KalpeMC &3&lYEDUPE &f&l| &b&lJUSTBOX &f&l| &3&lGENWARS &f&l| &b&lFORTKITS &f&l| &3&lSTAGES',
            ]
            pyautogui.typewrite(messages[choice - 1])  # Type message
            keyboard.press_and_release('enter')  # Send message
            sleep(1)  # Wait for message to send

            # Minimize Minecraft
            pyautogui.hotkey('win', 'down')
            pyautogui.hotkey('alt', 'tab')

            sleep(sleeptime)

    def pause_execution(self):
        print('\nPausing execution for 1-3 hours.\n')
        sleep(random.randint(5600, 10800))  # Pause for 1-3 hours (3600 to 10800 seconds)

if __name__ == "__main__":
    bot = AutoAdBot()
    bot.run()
