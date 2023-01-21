numbers = [1,2,3]
# for this list comprehension we want to multiply every element of the numbers list by a numvber (3)
new_numbers = [i*3 for i in numbers]
print(new_numbers)

# for this list comprehension we want to print every element of the new_numbers list  

x =[print(i)for i in new_numbers] 
print (x)

[print(i)for i in "Random String"] # can work with strings too

new_list = [n*2 for n in range(1,5)]

print(new_list)


#************************************************************************
# for example lets sort though a range of integers and only take the odd numbers to create a new list
#  
odd_nums = [n for n in range(1,20) if n %2 != 0]
print(odd_nums)
# ************************************************************************

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)
# ******************************************************
# the following example demonstrates checking for numbers common in two files and add to a new list using list comprehension
with open("file1.txt") as f1:
    list_1 = f1.readlines()
with open("file2.txt") as f2:
    list_2 = f2.readlines()

c = [int(x.strip()) for x in list_1 if x in list_2 ]

# Write your code above 👆
print(c )

