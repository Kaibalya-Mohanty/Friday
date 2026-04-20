import keyboard


def wait_for_wake_word():
    print("⌨️  Press Ctrl+Shift+F to activate FRIDAY...")
    keyboard.wait("ctrl+shift+f")
    print("✅ Activated!")
