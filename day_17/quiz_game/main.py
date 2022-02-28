from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []


for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text=question_text, question_answer=question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print(f"You finished the score: {quiz_brain.score}/{quiz_brain.question_number}")