from tkinter import *

window = Tk()
window.title("'Sup")
window.minsize(width=500, height=300)

input_thing = Entry(width=10)
input_thing.pack()

# Label
label = Label(text="HEY! HEEEEYYYY! I'M A LABEL", font=("Arial", 24))
label.pack(side="left")

def button_clicked():
    label.config(text=input_thing.get())

button = Button(text="cicke me. I dare you! WITNESS MEEEEEE!!!", command=button_clicked)
button.pack()

# input_thing = Entry(width=10)
# input_thing.pack()
# print(input_thing.get())

window.mainloop()
