import random


class QuizBrain:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.question_order = []
        self.question_number = 0
        self.score = 0
        for i in range(len(self.question_bank)):
            self.question_order.append(i)
        random.shuffle(self.question_order)

    def next_question(self):
        answer = input(f"Q{self.question_number + 1}. "
                       f"{self.question_bank[self.question_order[self.question_number]].text} (True/False): ")
        self.check_answer(answer, self.question_bank[self.question_order[self.question_number]].answer)

        self.question_number += 1

    def still_has_questions(self):
        return self.question_number != len(self.question_bank)

    def check_answer(self, user_answer, correct_answer):
        if (user_answer.lower() == correct_answer.lower()[:1]) or (user_answer.lower() == correct_answer.lower()):
            print("You got it right!")
            self.score += 1
            print(f"Score: {self.score}/{self.question_number + 1}\n")
        else:
            print("Sorry, that's not right.")
            print(f"The answer was {correct_answer}.")
            print(f"Score: {self.score}/{self.question_number + 1}\n")