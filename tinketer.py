import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
box = tk.Frame()

greeting = tk.Label(
    text="Hello, World",
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


#https://vehicleenquiry.service.gov.uk/?locale=en
#https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_the_United_Kingdom#Registration_plate_styles
#https://www.newreg.co.uk/dvla-number-plate-identifiers/
#https://realpython.com/python-gui-tkinter/
root.mainloop()
