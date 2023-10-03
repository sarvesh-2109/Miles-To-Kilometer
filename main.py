from tkinter import *


def miles_to_km():
    conversion = round(float(miles_input.get()) * 1.609, 2)
    km_result.config(text=conversion, font=("Arial", 11))


window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=350, height=100)
window.config(padx=30, pady=30)

# Labels
is_equal_label = Label(text="is equal to", font=("Arial", 11))
is_equal_label.grid(column=0, row=1)

miles = Label(text="Miles", font=("Arial", 11))
miles.grid(column=2, row=0)

km_result = Label(text=0)
km_result.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 11))
km.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)


window.mainloop()
