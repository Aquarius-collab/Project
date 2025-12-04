import tkinter as tk
import random

def gen():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    p = ""
    for i in range(10):
        p += random.choice(chars)
    v.set(p)

root = tk.Tk()
root.title("Password Maker")

tk.Button(root, text="Generate Password", command=gen).pack()

v = tk.StringVar()
tk.Label(root, textvariable=v, font=("Arial", 14)).pack()

root.mainloop()