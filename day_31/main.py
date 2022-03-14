
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"



# UI SETUP

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# #Canvas
card = Canvas(width=800, height=526)
image = PhotoImage(file="./images/card_front.png")
card.create_image(400, 262, image=image)
card.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card.create_text(400, 263, text="Title", font=("Ariel", 60, "bold"))
card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(row=0, column=0, columnspan=2)


# Buttons
button_image_1 = PhotoImage(file="./images/right.png")
right_btn = Button(image=button_image_1, highlightthickness=0, borderwidth=0)
right_btn.grid(row=1, column=1)
button_image_2 = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=button_image_2, highlightthickness=0, borderwidth=0, border=0)
wrong_btn.grid(row=1, column=0)

window.mainloop()

