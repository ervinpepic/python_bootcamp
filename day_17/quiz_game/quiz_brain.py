class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
    
    def still_has_questions(self):
        if self.question_number >= len(self.question_list):
            return False
        else:
            return True
    

    def next_question(self):
        for q in self.question_list:
            self.question_number += 1
            user_answer = input(f"Q.{self.question_number}) {q.text} (True/False)?: ")
            self.check_answer(user_answer, q.answer)
    

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("Wrong!")
            
        print(f"The correct answer was: {correct_answer}! ")
        print(f"You current score is: {self.score}/{self.question_number}\n")