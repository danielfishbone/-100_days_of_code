def prime_checker(number):
    prime_flag = False
    for num in range(2,number):
        if number % num == 0:
            prime_flag = False
            break
        else:
            prime_flag = True
    if prime_flag:
        print("It's a prime number.")   
    else:
        print("It's not a prime number.")         


n = int(input("Check this number: "))
prime_checker(number=n)