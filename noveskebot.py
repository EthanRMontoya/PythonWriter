from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
while True:
    emails = input("enter emails ")
    if emails == 'x':
        break
    delay = time.sleep(5)
    keyboard.type(emails)
    time.sleep(0.13)
    keyboard.press(Key.enter)