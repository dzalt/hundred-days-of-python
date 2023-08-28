# asking the quesions
# checking if the answer was correct
# checking if we're the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        self.counter = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        question = self.q_list[self.counter]
        self.counter += 1

        user_answer = input(f"Q.{self.counter}: {question.text} (True/False)?: ")
        self.check_answer(user_answer, question.answer)
    
    def still_has_questions(self):
        # if self.counter < len(self.q_list):
        #     return True
        # return False
        return self.counter < len(self.q_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.counter}")
        print("\n")