from tkinter import Tk, Entry, Label, Button

window = Tk()
window.title("Mile to Km Converter")

is_equal_to_label = Label(text="is equal to", font=("Arial"))
is_equal_to_label.grid(column=0, row=1, padx=20)

miles_input = Entry(width=15)
miles_input.grid(column=1, row=0, pady=20)

km_number = Label(font=("Arial"))
km_number.grid(column=1, row=1)

def button_clicked():
    # 1 mile = 1.609344 km
    # take input from miles_input
    # do math
    # display in km_number
    miles = int(miles_input.get())
    km = miles * 1.609344
    km_number.config(text=km)

button = Button(text="Calculate", font=("Arial"), command=button_clicked)
button.grid(column=1, row=2, pady=20)

miles_label = Label(text="Miles", font=("Arial"))
miles_label.grid(column=2, row=0, padx=20)

km_letters = Label(text="Km", font=("Arial"))
km_letters.grid(column=2, row=1)


window.mainloop()
