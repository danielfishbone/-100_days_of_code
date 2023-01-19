import csv
import pandas


# with open("/home/fishbone/python_100_days_of_code/day_25_of_100/weather_data.csv") as file:
#     data = file.readlines()



with open("/home/fishbone/python_100_days_of_code/day_25_of_100/weather_data.csv") as file:
    data = csv.reader(file)
    temperatures = []
    for row in data:
        if row[1].isnumeric():
            temperatures.append(int(row[1]))


print(temperatures)        

new_data = pandas.read_csv("/home/fishbone/python_100_days_of_code/day_25_of_100/weather_data.csv") 

print(new_data["temp"])