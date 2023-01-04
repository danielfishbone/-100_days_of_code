from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    question_object =Question(question["text"],question["answer"])
    question_bank.append(question_object)


print (question_bank)    