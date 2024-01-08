from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# calculate miles to kilometers
def calculate():
    m = float(miles_input.get())
    result_label["text"] = m*1.609

# input
miles_input = Entry(width=10)
miles_input.grid(row=1,column=2)

# label "miles"
miles_label = Label(text="miles")
miles_label.grid(row=1,column=3)

# label "is equal to"
equal_label = Label(text="is equal to")
equal_label.grid(row=2,column=1)

# label display calculation result
result_label = Label(text="")
result_label.grid(row=2,column=2)

# label "kilometers"
kilo_label = Label(text="kilometers")
kilo_label.grid(row=2,column=3)

# button "calculate"
calculate_button = Button(text="calculate", command=calculate)
calculate_button.grid(row=3,column=2)

window.mainloop()