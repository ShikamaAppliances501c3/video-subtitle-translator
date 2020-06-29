from pynput import keyboard
from pynput.keyboard import Key
from pynput.mouse import Controller

from vst.chinese_ocr import ChineseOCR
from vst.screenshot import Screenshot

import os
from tempfile import mkstemp


class KeyListener:
    def __init__(self, path):
        self.path = path
        self.mouse_controller = Controller()
        self.capturing = False
        self.start = []

    def on_press(self, key):
        mouse_controller = self.mouse_controller
        start = self.start
        capturing = self.capturing

        if key == Key.alt:
            if capturing:
                end = mouse_controller.position
                left = start[0]
                top = start[1]
                width = end[0] - left
                height = end[1] - top
                Screenshot.capture(path, left, top, width, height)
                return False
            else:
                self.start = mouse_controller.position
                self.capturing = True

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False


if __name__ == "__main__":
    fd, path = mkstemp()
    listener = KeyListener(path)
    with keyboard.Listener(
            on_press=listener.on_press,
            on_release=listener.on_release) as listener:
        listener.join()
    os.close(fd)
    text = ChineseOCR.ocr(path)
    print(text)
