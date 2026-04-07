"""
Defend Your Screen

A lightweight desktop access control tool that protects your screen
without interrupting running tasks.

Author: UnicusT11
Year: 2026

License: MIT License
This project is licensed under the MIT License.
You may obtain a copy of the License in the LICENSE file
in the root directory of this source tree.
"""

import time
import winsound
import pystray
import keyboard as kb
import tkinter as tk
import threading
from PIL import Image
from pystray import MenuItem, Menu
from pynput import keyboard
from pynput import mouse
from threading import Event

password = ''
start_hotkey = 'alt+c'
locked = False
hotkey_monitor = False
mouse_flag = Event()

# create a tray
def on_quit(icon, item):
    icon.stop()
    listener_0.stop()
    listener_1.stop()
    kb.remove_hotkey(start_hotkey)
    full.quit()
    kb.unhook_all()



def show_window():
    create_small()

img = Image.open("defend your screen.png")
menu = (MenuItem(text='View', action=show_window), MenuItem(text='Quit', action=on_quit))
icon = pystray.Icon("name", img, "defend your screen", menu)




# main threading
def on_click(x, y, button, pressed):
    global mouse_flag
    if pressed:
        mouse_flag.set()

def on_move(x, y):
    global mouse_flag
    mouse_flag.set()

def on_release(key):
    global mouse_flag
    try:
        mouse_flag.set()
    except AttributeError:
        mouse_flag.set()


# create listener
listener_0 = mouse.Listener(on_click=on_click,
                on_move=on_move)
listener_1 = keyboard.Listener(on_release=on_release)


# locked function
def f_locked():
    global locked
    if locked:
        return
    # winsound.PlaySound("SystemQuestion", winsound.SND_ASYNC)


    # locked the key
    kb.block_key('alt')
    kb.block_key('win')

    full.deiconify()
    full.focus_force()
    winsound.Beep(150, 300)


def f_unlocked():
    global locked
    global hotkey_monitor
    if entry_full.get() == password:
        locked = False
        hotkey_monitor = False
        full.withdraw()
        entry_full.delete(0, tk.END)

        # unlocked the key
        kb.unblock_key('alt')
        kb.unblock_key('win')
        # entry_full.delete(0, tk.END)
        # full.destroy()


# start monitor mode
def monitor():
    global hotkey_monitor
    winsound.PlaySound("SystemQuestion", winsound.SND_ASYNC)
    time.sleep(1)
    hotkey_monitor = True

kb.add_hotkey(start_hotkey, monitor)



# small window
def create_small():

    def init_window():
        global password
        global start_hotkey
        password = entry_password.get()

        # update hotkey
        new_hotkey = entry_hotkey.get()
        if new_hotkey != start_hotkey:
            kb.remove_hotkey(start_hotkey)
            start_hotkey = new_hotkey
            kb.add_hotkey(start_hotkey, monitor)

        small_root.withdraw()

    small_root = tk.Toplevel(full)
    small_root.geometry("300x350")
    small_root.title("Password Settings")

    frame = tk.Frame(small_root)
    frame.pack(expand=True, fill="both")
    entry_password = tk.Entry(small_root)

    tk.Label(small_root, text="Set a password\n(just use number)", font=("Arial", 10)).pack(pady=(5,5))
    entry_password.pack(pady=(5,15))
    entry_password.insert(0, password)
    entry_hotkey = tk.Entry(small_root)
    tk.Label(small_root, text="Set a start hotkey", font=("Arial", 10)).pack(pady=(15,5))
    entry_hotkey.pack(pady=(5,20))
    entry_hotkey.insert(0, start_hotkey)
    tk.Button(small_root, text="SAVE", command=init_window, width=10).pack(pady=(20,110))


# create multithreading
def listener_start():
    threading.Thread(target=listener_0.start(), daemon=True).start()
    threading.Thread(target=listener_1.start(), daemon=True).start()

def icon_thread():
    threading.Thread(target=icon.run, daemon=True).start()


# full window
full = tk.Tk()
full.withdraw()
full.attributes("-topmost", True)
full.attributes("-fullscreen", True)
full.configure(bg='black')
tk.Label(full, text="🔒Error: Unexpectedly locked 🔒", font=("Arial", 50), fg="red", bg="black").place(relx=0.25, rely=0.2)
tk.Label(full, text="⚠️️You can try entering the correct key to re-enable ⚠️", font=("Arial", 30), fg="red", bg="black").place(relx=0.25, rely=0.5)
entry_full = tk.Entry(full, show='*', width=50)
entry_full.place(relx=0.4, rely=0.75)
tk.Button(full, text="ENTER", command=f_unlocked, width=10, bg="black", fg="red", font=("Arial", 20)).place(relx=0.45, rely=0.8)

def loop():
    time.sleep(0.1)
    global locked
    if hotkey_monitor:
        if mouse_flag.is_set():
            # f_unlocked()
            if not locked:
                f_locked()
                locked = True
    mouse_flag.clear()
    full.after(100, loop)


icon_thread()
listener_start()
create_small()
loop()
full.mainloop()