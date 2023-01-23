import random
names = ['Ale','beth','caroline','osas','mark', 'fish']

#  create a dictionary using the names in the list as key and genreate random scores as value
student_scores = { student:random.randint(1 ,100) for student in names}
# print(student_scores)

#  create a dictionary of the students that got the pass mark

students_passed = {student.title():score for (student,score) in student_scores.items() if score > 60}
# print(students_passed)
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_set = sentence.split(sep=" ")
print(word_set)

words_dict = {word:len(word) for word in word_set}

print(words_dict)
