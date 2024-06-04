"""
This is Kitx - the KIT tx program

Open PS, open P000 entry
Open Fusion in background
Scan/input sample id in Kitx

Requires three small images in the same directory as this file:

- active PS window icon
- inactive PS window icon
- inactive Fusion window icon
"""

from tkinter import *
from tkinter import ttk
import pyautogui
import sys

# top level constants

# icons
PS_ACTIVE = "ProSang_active.png"
PS_INACTIVE = "ProSang_inactive.png"
FUSION_INACTIVE = "Fusion_inactive.png"

# frame padding
PADDING = 5

# start position, from top left
STARTX = 1700
STARTY = 800


class Kitx(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=PADDING)
        self.master = master

        self.grid()  # unnecessary with one widget but who cares

        self.labnr_entry = ttk.Entry(self)
        self.labnr_entry.grid(column=0, row=0)
        self.labnr_entry.bind("<Return>", self.entry_enter_event)
        self.clear()

        # self.check_modal = ttk.Checkbutton(
        #     self, text="Modal", command=self.toggle_modal
        # )
        # self.check_modal.invoke()
        # self.check_modal.grid(column=0, row=1)

        # have Esc clear the entry
        master.bind("<Escape>", lambda e: self.clear())

    def entry_enter_event(self, event):
        """Callback for event press in entry"""

        short = 0.2
        long = 0.5

        # let's go

        print(f"input is '{self.labnr_entry.get()}'", file=sys.stderr)

        # ProSang
        try:
            print("click PS active window", file=sys.stderr)
            pyautogui.click(PS_ACTIVE, duration=short)
        except:
            # activate background window
            print("except: click ProSang inactive window")
            pyautogui.click(PS_INACTIVE, duration=short)

        print("click drop-down box", file=sys.stderr)
        pyautogui.click(700, 420, duration=short)

        print("click sample id", file=sys.stderr)
        pyautogui.click(700, 475, duration=short)

        print("click text entry", file=sys.stderr)
        pyautogui.click(740, 420, duration=short)

        print("write sample id entry", file=sys.stderr)
        pyautogui.write(self.labnr_entry.get())
        pyautogui.write(["enter"])

        print("allow some time to search, OK will become green", file=sys.stderr)
        pyautogui.sleep(long)

        print("click OK", file=sys.stderr)
        pyautogui.click(1160, 670, duration=short)

        # Fusion
        print("click Fusion inactive window", file=sys.stderr)
        pyautogui.click(FUSION_INACTIVE, duration=short)

        print("click find icon", file=sys.stderr)
        pyautogui.click(60, 50, duration=long)

        print("click sample id label", file=sys.stderr)
        pyautogui.click(700, 395, duration=short)

        print("click text area", file=sys.stderr)
        pyautogui.click(800, 400, duration=short)

        print("write sample id", file=sys.stderr)
        pyautogui.write(self.labnr_entry.get())
        pyautogui.write("*")  # search all starting with entry

        print("click search button", file=sys.stderr)
        pyautogui.click(840, 725, duration=short)

        print("click expand image", file=sys.stderr)
        pyautogui.click(1695, 150, duration=short + long)

    def clear(self):
        """Restore labnr_entry"""
        self.labnr_entry.delete(0, "end")
        self.labnr_entry.focus()

    # def toggle_modal(self):
    #     """Toggle the modal status
    #     """
    #     if self.check_modal.instate(["selected"]):
    #         self.master.attributes("-topmost", "true")
    #     else:
    #         self.master.attributes("-topmost", "false")


# window
root = Tk()

# position window
root.geometry(f"+{STARTX}+{STARTY}")

# start on top!
root.attributes("-topmost", "true")

root.title("kitx")

# removes maximize button but disables alt-tab for window
# root.attributes("-toolwindow", True)

# make non-resizable
root.resizable(0, 0)

# the program is a frame
kitx = Kitx(root)

# run mainloop
root.mainloop()
