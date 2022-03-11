from lib2to3.pytree import convert
import tkinter

def button_clicked():
    converted_text = ipt.get()
    miles = int(converted_text)
    km = round(miles * 1.609344, 2)
    convert_num["text"] = km

# Create Window
window = tkinter.Tk()
window.title("Convert Miles to Kilometers")
window.minsize(width=200, height=200)
window.config(padx=100, pady=100)

miles = tkinter.Label(text="Miles", font=("Helvetica", 18, "bold"))
miles.config(padx=10)
miles.grid(column=3, row=2)

is_equal_to = tkinter.Label(text="Is equal to", font=("Helvetica", 18, "bold"))
is_equal_to.grid(column=2, row=3)

convert_num = tkinter.Label(text="0", font=("Helvetica", 18, "bold"))
convert_num.grid(column=3, row=3)

label = tkinter.Label(text="kilometers", font=("Helvetica", 18, "bold"))
label.grid(column=4, row=3)

# Buttons
convert_miles = tkinter.Button(text="Convert", command=button_clicked)
convert_miles.grid(column=3, row=4)

# Entry
ipt = tkinter.Entry(width=10)
ipt.grid(column=2, row=2)



window.mainloop()