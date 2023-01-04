from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_object =Question(question["text"],question["answer"])
    question_bank.append(question_object)


quiz = QuizBrain(question_bank)

print(quiz.next_question())