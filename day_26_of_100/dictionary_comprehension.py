import pandas 
import random
names = ['Ale','beth','caroline','osas','mark', 'fish']

#  create a dictionary using the names in the list as key and genreate random scores as value
student_scores = { student:random.randint(1 ,100) for student in names}
# print(student_scores)

#  create a dictionary of the students that got the pass mark

students_passed = {student.title():score for (student,score) in student_scores.items() if score > 60}
print(students_passed)

# **************************************************************************************************************
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_set = sentence.split(sep=" ")
# print(word_set)

words_dict = {word:len(word) for word in word_set}

# print(words_dict)
# **************************************************************************************************************
#  use dictionary comprehension to convert the celcius value og the temperatures to fahrenheit
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day:(temp_c * 9/5) + 32  for (day,temp_c) in weather_c.items()}
# print(weather_f)
# ***********************************************Looping through pandas dataframes 
students_dict = {
"name":['Ale','beth','caroline','osas','mark', 'fish'],
"score":[44,12,64,81,68,101]

}
student_dataframe = pandas.DataFrame(students_dict)
# print(student_dataframe)

# for (rows,cols) in student_dataframe.items():
#     print(rows)    
#     print(cols)

for (index,row) in student_dataframe.iterrows():
    print(row.name)
    print(row.score)