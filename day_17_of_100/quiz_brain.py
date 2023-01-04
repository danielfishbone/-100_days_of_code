

class QuizBrain:
    def __init__(self,questions = []):
        self.question_number = 0
        self.questions_list = questions
        self.score = 0
        
    def next_question(self):
        
        text = self.questions_list[self.question_number].text
        answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {text}? (True/False): ").lower()
        self.check_answer(answer, user_answer) 

    def still_has_questions(self):
        return self.question_number < len(self.questions_list)

    def check_answer(self,answer, user_answer):
        if answer.lower() == user_answer : 
            print("You're correct!")
            self.score += 1
        else:
            print(f"Wrong, the correct answer is {answer} ")    

               