

class QuizBrain:
    def __init__(self,questions = []):
        self.question_number = 0
        self.questions_list = questions
        
    def next_question(self):
        
        text = self.questions_list[self.question_number].text
        answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {text}? (True/False): ").lower()
        return answer, user_answer

    def still_has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            return False       