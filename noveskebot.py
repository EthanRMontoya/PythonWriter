from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
fo = open("emails.txt", "r")
while True:
        coolguy = input("y Enter to Cont, X to quit")
        if coolguy == 'y':
            fo.seek(0,0)
            for line in fo.readlines():
                delay = time.sleep(2)
                keyboard.type(line)
                keyboard.tap(Key.enter)
                time.sleep(0.13)
        else:
            exit()