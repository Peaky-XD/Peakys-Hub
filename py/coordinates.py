#!/usr/bin/env python3
#coded by : @x_spoilt 
#---------------------
import tkinter as tk
def update_coordinates(event):
    x = event.x
    y = event.y
    x_var.set(f"X: {x}")
    y_var.set(f"Y: {y}")
root = tk.Tk()
root.title("Mouse Coordinates")
x_var = tk.StringVar()
y_var = tk.StringVar()
label_x = tk.Label(root, textvariable=x_var, font=("Helvetica", 16))
label_y = tk.Label(root, textvariable=y_var, font=("Helvetica", 16))
root.bind('<Motion>', update_coordinates)
label_x.pack(pady=10)
label_y.pack(pady=10)
root.mainloop()
