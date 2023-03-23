import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)


name = ttk.Label(root, text="Hello, world")
name.pack()

style.theme_use("clam")

style.configure("TLabel", bordercolor="#f00")
style.configure("TLabel", borderwidth=20)
style.configure("TLabel", relief="solid")

print(style.layout("TLabel"))

root.mainloop()