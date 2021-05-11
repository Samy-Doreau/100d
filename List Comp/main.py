import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

students_scores = {key: random.randint(0, 100) for key in names}
passed_students = {name: score > 60 for (
    name, score) in students_scores.items()}
print(students_scores)
print(passed_students)
