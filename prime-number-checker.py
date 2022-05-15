def prime_checker(number):
    for i in range(2, number):
        if number %  i == 0:
            is_prime = False
        else:
            is_prime = True
    if is_prime == True:
        print("its a prime number")
    else:
        print("its not a prime number")
    
    






n = int(input("check this number: "))

prime_checker(number = n)
