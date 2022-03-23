from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data['results']:
    question_bank.append(Question(data['question'], data['correct_answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f'You\'ve completed the quiz '
      f'\nYour final score was {quiz.score}/{quiz.question_number}')