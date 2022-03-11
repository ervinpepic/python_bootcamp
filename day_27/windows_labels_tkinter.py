import tkinter

def button_clicked():
    label["text"] = ipt.get()

# Create Window
window = tkinter.Tk()
window.title("First TKINTER program")
window.minsize(width=500, height=500)

# create components

# Label
label = tkinter.Label(text="Your name", font=("Helvetica", 18, "bold"))
label["text"] = "New tekst"
label.grid(column=0, row=0)

# Buttons
button = tkinter.Button(text="Press", command=button_clicked)
button.grid(column=3, row=0)

button = tkinter.Button(text="Click", command=button_clicked)
button.grid(column=1, row=1)

# Entry
ipt = tkinter.Entry(width=10)
ipt.grid(column=5, row=3)



# Keep window opened
window.mainloop()