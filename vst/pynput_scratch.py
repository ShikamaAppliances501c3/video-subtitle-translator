from pynput import keyboard
from pynput import mouse
from functools import partial

def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(start_end, x, y, button, pressed):
    if not start_end:
        start_end.append((x, y))
    print(f"{'Pressed' if pressed else 'Released'} at {(x,y)}")
    if not pressed:
        # Stop listener
        start_end.append((x,y))
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        if key == keyboard.KeyCode.from_char('f'):
            # Collect events until released
            start_end = []
            with mouse.Listener(
                    on_move=on_move,
                    on_click=partial(on_click, start_end),
                    on_scroll=on_scroll) as listener:
                listener.join()
            print(start_end)
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
