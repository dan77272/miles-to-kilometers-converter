from tkinter import *


def calculate():
    input = float(entry.get())
    kilometers = round(input * 1.609)
    kilo.config(text=kilometers)


window = Tk()
window.minsize(300, 100)
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

entry = Entry()
entry.grid(column=1, row=0)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

kilo_label = Label(text="Kilometers")
kilo_label.grid(column=2, row=1)

kilo = Label(text="0")
kilo.grid(column=1, row=1)

window.mainloop()
