from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# turn questions into objects then put them on a list

question_bank = []

for i in question_data:
    new_q = Question(i["text"], i["answer"])
    question_bank.append(new_q)

# quiz start

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.counter}")
