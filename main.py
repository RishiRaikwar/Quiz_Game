from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    que = Question(item["text"], item["answer"])
    question_bank.append(que)

my_quiz = QuizBrain(question_bank)

while my_quiz.still_has_questions_left():
    my_quiz.next_question()

print("You have completed the quiz.")
print(f"You final score is {my_quiz.score}/{my_quiz.question_number}")
