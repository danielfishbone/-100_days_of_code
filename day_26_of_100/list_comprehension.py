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