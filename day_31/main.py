from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

current_word = {}
words_to_learn = {}

# Read CSV file
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    first_file = pandas.read_csv("./data/french_words.csv")
    words_to_learn = first_file.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


def generate_next_word():
    try:
        global current_word, flip_after

        window.after_cancel(flip_after)

        word = random.choice(words_to_learn)   
        card.itemconfig(label_word, text=word["French"], fill="black")
        card.itemconfig(label_title, text="French", fill='black')
        card.itemconfig(canvas_image, image=french_image)
        current_word = word
        flip_after = window.after(3000, timer)

    except IndexError:
        card.itemconfig(label_title, text="DONE!", fill='black')
        card.itemconfig(label_word, text="", fill='black')
        right_btn.config(state='disabled')
        wrong_btn.config(state='disabled')
        messagebox.showinfo(title="CONGRATS!", message="YOU HAVE LEARNED ALL THE WORDS")

def remove_learned_words():
    words_to_learn.remove(current_word)
    generate_next_word()
    final = pandas.DataFrame(words_to_learn)
    final.to_csv("./data/words_to_learn.csv", index=False)
    
def timer():
    global current_word
    card.itemconfig(label_title, text="English", fill="#FFFFFF")
    card.itemconfig(label_word, text=current_word["English"], fill="#FFFFFF")
    card.itemconfig(canvas_image, image=eng_image)


# UI SETUP
# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_after = window.after(3000, timer)

# #Canvas
card = Canvas(width=800, height=526)
french_image = PhotoImage(file="./images/card_front.png")
eng_image = PhotoImage(file="./images/card_back.png")
canvas_image = card.create_image(400, 262, image=french_image)
label_title = card.create_text(
    400, 150, text="french_lang", font=("Ariel", 40, "italic"), fill="Black")
label_word = card.create_text(
    400, 263, text="Word", font=("Ariel", 60, "bold"), fill="Black")
card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(row=0, column=0, columnspan=2)


# Buttons
button_image_1 = PhotoImage(file="./images/right.png")
right_btn = Button(image=button_image_1, highlightthickness=0,
                   borderwidth=0, command=remove_learned_words)
right_btn.grid(row=1, column=1)
button_image_2 = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=button_image_2, highlightthickness=0,
                   borderwidth=0, border=0, command=generate_next_word)
wrong_btn.grid(row=1, column=0)
generate_next_word()
window.mainloop()
