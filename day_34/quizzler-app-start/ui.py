from time import time
from tkinter import *
import time
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_lbl = Label(text="Score: 0", fg="white", background=THEME_COLOR)
        self.score_lbl.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question_text", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_btn_image = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=self.true_btn_image, highlightthickness=0,
                        borderwidth=0, command=self.true_answer)
        self.true_btn.grid(row=2, column=0, pady=10)

        self.false_btn_image = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=self.false_btn_image, highlightthickness=0,
                        borderwidth=0, border=0, command=self.false_answer)
        self.false_btn.grid(row=2, column=1, pady=10)

        self.get_next_question()


        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
            self.score_lbl.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You reached the end of the quiz")
            self.canvas.config(bg="white")
            self.true_btn.config(state='disabled')
            self.false_btn.config(state='disabled')


    def true_answer(self):
        u_a = self.quiz.check_answer(user_answer="True")
        self.give_feedback(u_a)
    
    def false_answer(self):
       u_a = self.quiz.check_answer(user_answer="False")
       self.give_feedback(u_a)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
        
            