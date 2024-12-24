from licenseBackend import *
import tkinter as tk

root = tk.Tk()
root.title("LICENSE PLATE")

licenseVar=tk.StringVar()
dataArray = []
def submit():
    licensePlate=licenseVar.get()
    try:
        dataArray = runLicense(licensePlate)
        licenseResponceLable.config(text = dataArray[0])
        licenseResponceLableOne.config(text = dataArray[1])
        licenseResponceLableTwo.config(text = dataArray[2])
        licenseResponceLableThree.config(text = dataArray[3])
        licenseResponceLableFour.config(text = dataArray[4])
    except:
            licenseResponceLable.config(text = "Invaild")
    licenseVar.set("")



licenseLable = tk.Label(root, text="License Plate", font=('calibre',10,'bold'))

licenseEntry = tk.Entry(root,textvariable = licenseVar, font=('calibre',10,'normal'))

subBtn = tk.Button(root,text = 'Submit', command = submit)
licenseResponceLable = tk.Label(root,text="Enter Data", font=('calibre',10,'bold'), bg="yellow", fg="black")
licenseResponceLableOne = tk.Label(root,text="", font=('calibre',10,'bold'))
licenseResponceLableTwo = tk.Label(root,text="", font=('calibre',10,'bold'))
licenseResponceLableThree = tk.Label(root,text="", font=('calibre',10,'bold'))
licenseResponceLableFour = tk.Label(root,text="", font=('calibre',10,'bold'))

licenseLable.grid(row=0,column=0)
licenseEntry.grid(row=1,column=0)
subBtn.grid(row=2,column=0)
licenseResponceLable.grid(row=3,column=0)
licenseResponceLableOne.grid(row=4,column=0)
licenseResponceLableTwo.grid(row=5,column=0)
licenseResponceLableThree.grid(row=6,column=0)
licenseResponceLableFour.grid(row=7,column=0)
root.mainloop()

#inVal = input("\nLicence Number UK (no Space): ")


