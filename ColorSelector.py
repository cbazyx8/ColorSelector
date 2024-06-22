import tkinter as tk
from tkinter import colorchooser

def select_color():
    color = colorchooser.askcolor(title="Select a color")
    if color[1]:
        color_label.config(bg=color[1], fg=color[0])
        color_value.set(color[1])

root = tk.Tk()
root.title("Color Palette Selector")

color_value = tk.StringVar()
color_label = tk.Label(root, text="Click to select a color", padx=20, pady=20, textvariable=color_value)
color_label.pack()

select_button = tk.Button(root, text="Select Color", command=select_color)
select_button.pack(pady=10)

root.mainloop()
