with  open("/home/fishbone/python_100_days_of_code/day_24_of_100/my_file.txt", mode = "r") as file :
    contents = file.read()
    print(contents)


with open("/home/fishbone/python_100_days_of_code/day_24_of_100/my_file.txt", mode = "w") as file :
     file.write(str(9))

with  open("/home/fishbone/python_100_days_of_code/day_24_of_100/my_file.txt", mode = "r") as file :
    contents = file.read()
    print(int(contents)+5)