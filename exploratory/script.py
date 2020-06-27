from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

rename_variable = Tk()
rename_variable.title("Feet to Meters")


def extract_method():
    global helloworld
    helloworld = ttk.Frame(rename_variable, padding="3 3 12 12")
    helloworld.grid(column=0, row=0, sticky=(N, W, E, S))
    rename_variable.columnconfigure(0, weight=1)
    rename_variable.rowconfigure(0, weight=1)


extract_method()

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(helloworld, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(helloworld, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(helloworld, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(helloworld, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(helloworld, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(helloworld, text="meters").grid(column=3, row=2, sticky=W)

for child in helloworld.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
rename_variable.bind('<Return>', calculate)

rename_variable.mainloop()