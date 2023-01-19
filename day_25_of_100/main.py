import csv
import pandas


# with open("/home/fishbone/python_100_days_of_code/day_25_of_100/weather_data.csv") as file:
#     data = file.readlines()



# with open("/home/fishbone/python_100_days_of_code/day_25_of_100/weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1].isnumeric():
#             temperatures.append(int(row[1]))


# print(temperatures)        

new_data = pandas.read_csv("/home/fishbone/python_100_days_of_code/day_25_of_100/weather_data.csv") 

# # print(new_data["temp"])

# data_dict = new_data.to_dict()
# temp_list = new_data["temp"].to_list()

# # print(f"New dict: {data_dict}")
# # print(f"New list: {temp_list}")

# # ***************************************************************************************
# # temp_sum = 0
# # for temp in temp_list:
# #     temp_sum += temp

# # temp_sum /= len(temp_list)
# # print(f"Average Temperature: {temp_sum}")
# # 
# print(f'Average Temperature: {new_data["temp"].mean()}')
# print(f'Max Temperature1: {new_data["temp"].max()}') or print(f'Max Temperature: {new_data.temp.min()}')
# print(new_data[new_data.day == "Monday"])
# ******************************************************************************************************************
# print(new_data[new_data.temp == new_data.temp.max()])

# monday = new_data[new_data.day == "Monday"]
# temp = int(monday.temp)
# print(temp)

# # (0°C × 9/5) + 32 = 32°F
# temp_f = (temp * 9/5) + 32
# print(f"Temperature in fahrenheit: {temp_f}")

# *******************************************************************************************************************

data_dict = {
                "students":["Amy","James","Angela"],
                "scores":[76,93,79]

}
new_dat = pandas.DataFrame(data_dict)
new_dat.to_csv("new_dataset.csv")
