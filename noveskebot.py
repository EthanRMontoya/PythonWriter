from pynput.keyboard import Key, Controller
from pynput.mouse import Button
from pynput import mouse

import time

keyboard = Controller()
fo = open("emails.txt", "r")
delayTime = input("enter your delay time in seconds")
while True:
        coolguy = input("y Enter to Cont, X to quit")
        if coolguy == 'x':
            delayTime = 0
        time.sleep(int(delayTime))
        if coolguy == 'y':
            fo.seek(0,0)
            for line in fo.readlines():
                keyboard.type(line)
                keyboard.tap(Key.enter)
                keyboard.press(Key.cmd)
                keyboard.press(Key.left)
                time.sleep(3.0)
                keyboard.release(Key.cmd)
                keyboard.release(Key.left)
                time.sleep(3.0)
                keyboard.press(Key.cmd)
                keyboard.press('a')
                keyboard.tap(Key.backspace)
                keyboard.release('a')
                keyboard.release(Key.cmd)
        else:
            exit()