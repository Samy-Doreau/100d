from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain
question_bank = []
for q in question_data:
    question_bank.append(Question(q['text'], q['answer']))

quiz = QuizzBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(
    f"You've completed the quizz, \n your final score is : {quiz.score} / {quiz.question_nb}.")
