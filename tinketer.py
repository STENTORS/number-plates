#not yet usable - just testing framwork
import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
box = tk.Frame()

greeting = tk.Label(
    text="Enter Plate",
    fg="white",
    bg = "black",
    height=2,
    width=15
)
snaz = ttk.Label(
    master=box,
    text= "snazzy",
    foreground="white",
    background="green",
)
snaz.pack()


licence = tk.Button(
    text="Push",
    width=25,
    height=5,
    bg="blue",
    fg="yellow"
)

enter = tk.Entry(fg="yellow",bg="blue",width=50)
userIn = enter.get()

box.pack()
greeting.pack()
enter.pack()

if licence:
    print(userIn)
licence.pack()

root.mainloop()
