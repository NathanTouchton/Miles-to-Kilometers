from tkinter import *

window = Tk()
window.title("'Sup")
window.minsize(width=500, height=300)

# Label
label = Label(text="HEY! HEEEEYYYY! I'M A LABEL", font=("Arial"))
label.grid(column=0, row=0)

def button_clicked():
    label.config(text=entry.get())

button = Button(text="button 1", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="button 2")
new_button.grid(column=2, row=0)

entry = Entry(width=10)
entry.grid(column=3, row=2)

# entry = Entry(width=10)
# entry.pack()
# print(entry.get())

window.mainloop()
