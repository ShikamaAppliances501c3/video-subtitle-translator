from pynput import keyboard
from pynput.keyboard import Key
from pynput.mouse import Controller
from vst.screenshot import Screenshot


class KeyListener:
    mouse_controller = Controller()
    capturing = False
    start = []

    @staticmethod
    def on_press(key):
        mouse_controller = KeyListener.mouse_controller
        start = KeyListener.start
        capturing = KeyListener.capturing

        if key == Key.alt:
            if capturing:
                end = mouse_controller.position
                left = start[0]
                top = start[1]
                width = end[0] - left
                height = end[1] - top
                Screenshot.capture(left, top, width, height)
                return False
            else:
                KeyListener.start = mouse_controller.position
                KeyListener.capturing = True

    @staticmethod
    def on_release(key):
        if key == keyboard.Key.esc:
            return False

if __name__ == "__main__":
    # Collect events until released
    with keyboard.Listener(
            on_press=KeyListener.on_press,
            on_release=KeyListener.on_release) as listener:
        listener.join()
