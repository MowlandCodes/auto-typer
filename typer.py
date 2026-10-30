"""
Auto-typer: A simple Python library to simulate typing in Linux.

This library is inspired and modified from the original work of eyekay/libclicker (https://codeberg.org/eyekay/libclicker)

Modifications only removing the mouse functionality and adding a delay between key presses.

Credits to eyekay (https://codeberg.org/eyekay) for the original work.
"""

import string
import time

import uinput

keys = [
    uinput.KEY_LEFTSHIFT,
    uinput.KEY_SPACE,
    uinput.BTN_LEFT,
    uinput.BTN_MIDDLE,
    uinput.BTN_RIGHT,
    uinput.REL_X,
    uinput.REL_Y,
    uinput.REL_WHEEL,
    uinput.REL_HWHEEL,
    uinput.KEY_TAB,
    uinput.KEY_ENTER,
]

punctuation = {
    ",": "COMMA",
    ".": "DOT",
    "/": "SLASH",
    ";": "SEMICOLON",
    "'": "APOSTROPHE",
    "[": "LEFTBRACE",
    "]": "RIGHTBRACE",
    "\\": "BACKSLASH",
    "-": "MINUS",
    "=": "EQUAL",
    "`": "GRAVE",
}
punctuation_shift = {
    "<": "COMMA",
    ">": "DOT",
    "?": "SLASH",
    ":": "SEMICOLON",
    '"': "APOSTROPHE",
    "{": "LEFTBRACE",
    "}": "RIGHTBRACE",
    "|": "BACKSLASH",
    "_": "MINUS",
    "+": "EQUAL",
    "~": "GRAVE",
}
punctuation_ = ",./;'[]\\-=`"
punctuation_shift_ = '<>?:"{}|_+~'
digit_symbols = {
    "!": "1",
    "@": "2",
    "#": "3",
    "$": "4",
    "%": "5",
    "^": "6",
    "&": "7",
    "*": "8",
    "(": "9",
    ")": "0",
}

keys.extend([eval(f"uinput.KEY_{i.upper()}") for i in string.ascii_lowercase])
keys.extend([eval(f"uinput.KEY_{i}") for i in string.digits])
keys.extend([eval(f"uinput.KEY_{digit_symbols[i]}") for i in digit_symbols])
keys.extend([eval(f"uinput.KEY_{punctuation[i]}") for i in punctuation_])
keys.extend([eval(f"uinput.KEY_{punctuation_shift[i]}") for i in punctuation_shift_])

device = uinput.Device(keys)

time.sleep(1)


def press_key(key: str):
    printables = string.printable + "\t\n"

    if type(key) != str:
        raise ValueError("key must be a string")
    if key not in printables:
        raise ValueError("key must be printable")
    if len(key) > 1:
        raise ValueError("key must be a single character")

    if key in string.ascii_lowercase:
        device.emit(eval(f"uinput.KEY_{key.upper()}"), 1)
        device.emit(eval(f"uinput.KEY_{key.upper()}"), 0)
    elif key in string.ascii_uppercase:
        device.emit(uinput.KEY_LEFTSHIFT, 1)
        device.emit(eval(f"uinput.KEY_{key.upper()}"), 1)
        device.emit(eval(f"uinput.KEY_{key.upper()}"), 0)
        device.emit(uinput.KEY_LEFTSHIFT, 0)
    elif key in string.digits:
        device.emit(eval(f"uinput.KEY_{key}"), 1)
        device.emit(eval(f"uinput.KEY_{key}"), 0)
    elif key in digit_symbols:
        device.emit(uinput.KEY_LEFTSHIFT, 1)
        device.emit(eval(f"uinput.KEY_{digit_symbols[key]}"), 1)
        device.emit(eval(f"uinput.KEY_{digit_symbols[key]}"), 0)
        device.emit(uinput.KEY_LEFTSHIFT, 0)
    elif key in punctuation_:
        device.emit(eval(f"uinput.KEY_{punctuation[key]}"), 1)
        device.emit(eval(f"uinput.KEY_{punctuation[key]}"), 0)
    elif key in punctuation_shift_:
        device.emit(uinput.KEY_LEFTSHIFT, 1)
        device.emit(eval(f"uinput.KEY_{punctuation_shift[key]}"), 1)
        device.emit(eval(f"uinput.KEY_{punctuation_shift[key]}"), 0)
        device.emit(uinput.KEY_LEFTSHIFT, 0)
    elif key == " ":
        device.emit(uinput.KEY_SPACE, 1)
        device.emit(uinput.KEY_SPACE, 0)
    elif key == "\t":
        device.emit(uinput.KEY_TAB, 1)
        device.emit(uinput.KEY_TAB, 0)
    elif key == "\n":
        device.emit(uinput.KEY_ENTER, 1)
        device.emit(uinput.KEY_ENTER, 0)


# Type text
def type_text(text: str, delay: float = 0):
    if type(text) != str:
        raise ValueError("text must be a string")
    for i in text:
        if i not in string.printable:
            raise ValueError(f"charactert {i} is not printable")

    for key in text:
        press_key(key)
        time.sleep(delay)
