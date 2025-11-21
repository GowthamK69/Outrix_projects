import tkinter as tk
from tkinter import *

# ====================================================
# 🐐 GOATED TKINTER CALCULATOR – PREMIUM EDITION (FIXED)
# Author : Gowtham
# ====================================================

root = Tk()
root.title("GOAT Calculator")
root.geometry("350x450")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

expression = ""
input_text = StringVar()

# Display Box (PACK)
display = Entry(
    root, font=("Helvetica", 24),
    textvariable=input_text,
    bg="#333333", fg="white",
    bd=0, justify=RIGHT
)
display.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=20)

def press(num):
    global expression
    expression += str(num)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Button style function
def make_button(parent, text, command, color="#444444"):
    return Button(
        parent, text=text, command=command,
        font=("Helvetica", 18, "bold"),
        bg=color, fg="white",
        activebackground="#666666",
        activeforeground="white",
        bd=0, width=5, height=2
    )

# NOW create a frame for all grid buttons (IMPORTANT FIX)
button_frame = Frame(root, bg="#1e1e1e")
button_frame.pack()

# ROW 1
make_button(button_frame, "7", lambda: press(7)).grid(row=0, column=0, padx=5, pady=5)
make_button(button_frame, "8", lambda: press(8)).grid(row=0, column=1, padx=5, pady=5)
make_button(button_frame, "9", lambda: press(9)).grid(row=0, column=2, padx=5, pady=5)
make_button(button_frame, "/", lambda: press("/"), "#ff9800").grid(row=0, column=3, padx=5, pady=5)

# ROW 2
make_button(button_frame, "4", lambda: press(4)).grid(row=1, column=0, padx=5, pady=5)
make_button(button_frame, "5", lambda: press(5)).grid(row=1, column=1, padx=5, pady=5)
make_button(button_frame, "6", lambda: press(6)).grid(row=1, column=2, padx=5, pady=5)
make_button(button_frame, "*", lambda: press("*"), "#ff9800").grid(row=1, column=3, padx=5, pady=5)

# ROW 3
make_button(button_frame, "1", lambda: press(1)).grid(row=2, column=0, padx=5, pady=5)
make_button(button_frame, "2", lambda: press(2)).grid(row=2, column=1, padx=5, pady=5)
make_button(button_frame, "3", lambda: press(3)).grid(row=2, column=2, padx=5, pady=5)
make_button(button_frame, "-", lambda: press("-"), "#ff9800").grid(row=2, column=3, padx=5, pady=5)

# ROW 4
make_button(button_frame, "0", lambda: press(0)).grid(row=3, column=0, padx=5, pady=5)
make_button(button_frame, ".", lambda: press(".")).grid(row=3, column=1, padx=5, pady=5)
make_button(button_frame, "=", equal, "#4caf50").grid(row=3, column=2, padx=5, pady=5)
make_button(button_frame, "+", lambda: press("+"), "#ff9800").grid(row=3, column=3, padx=5, pady=5)

# CLEAR BUTTON (PACK)
Button(
    root, text="CLEAR", command=clear,
    bg="#e53935", fg="white",
    font=("Helvetica", 16, "bold"),
    bd=0, width=22, height=2,
    activebackground="#ff5252"
).pack(pady=10)

root.mainloop()
