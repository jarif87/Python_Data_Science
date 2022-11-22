check_prime_number=int(input("Enter your number:\n"))
if check_prime_number>1:
    for i in range(2,check_prime_number):
        if(check_prime_number%i==0):
            print("Number is not Prime",check_prime_number)
            break
    else:
        print("Number is Prime",check_prime_number)
    
