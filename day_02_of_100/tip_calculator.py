# day 2 coding task, tip calculator
total = input("What was the total bill? ")
percentage = input("what percentage tip would you like to give? 10,12 or 15? ")
people = input("How many people to split the bill? ")
_total = float(total)
_percentage = _total * (float(percentage) / 100)
_people = int(people)
pay_amount = (_total + _percentage) / _people
pay_amount = "{:.2f}".format(pay_amount)
print(f"Each person should pay: ${pay_amount}")