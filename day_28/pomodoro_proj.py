from tkinter import *
import math
import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ---------------------------- GLOBAL VARS ------------------------------- #
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def timer_reset():
    window.after_cancel(timer)
    title["text"] = "TIMER"
    canvas.itemconfig(timer_text, text="00:00")
    checkmark["text"] = ""
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        counter_minus(long_break_sec)
        title.config(text="Please take a break!", fg=PINK)
    elif reps % 2 == 0:
        counter_minus(short_break_sec)
        title.config(text="Please take a break!", fg=RED)
    else:
        counter_minus(work_sec)
        title.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counter_minus(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, counter_minus, count - 1)
    else:
        start_timer()
        checkmark_sign = ""
        sessions = math.floor(reps / 2)
        for _ in range(sessions):
            checkmark_sign += "✔"
        checkmark.config(text=checkmark_sign)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Tomato timer")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=3, column=3)


# Labels setup
title = tkinter.Label(text="Timer", fg=GREEN, font=(
    FONT_NAME, 50, "normal"), bg=YELLOW)
title.grid(row=0, column=3)

checkmark = tkinter.Label(fg=GREEN, font=(
    FONT_NAME, 45, "normal"), bg=YELLOW)
checkmark.grid(row=6, column=3)

# Buttons setup
start_button = tkinter.Button(
    text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=5, column=1)

reset_button = tkinter.Button(
    text="Reset", bg=YELLOW, highlightbackground=YELLOW, command=timer_reset)
reset_button.grid(row=5, column=4)

# Keep window open
window.mainloop()
