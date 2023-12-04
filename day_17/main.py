from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for qd in question_data:
    question_bank.append(Question(qd["text"], qd["answer"]))

qb = QuizBrain(question_bank)
while qb.still_has_questions():
    qb.next_question()

print("You've completed the quiz!")
print(f"You scored {qb.score}/{len(question_bank)}")