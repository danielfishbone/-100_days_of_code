from math import nan
import pandas as pd

data = pd.read_csv("/home/fishbone/python_100_days_of_code/day_25_of_100/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"]

# print(type(fur_color.to_list()))
colors_list = fur_color.to_list()
colors = []
colors_count = []
for color in colors_list:
    # if color not in colors and isinstance(color, str):
    if color not in colors:
        colors.append(color)
for _ in  colors:
       colors_count.append(0)
for color in colors_list:
    index = colors. index(color)
    colors_count[index] += 1 

print(f"colors{colors}")    
print(f"colors_count{colors_count}")    





     

