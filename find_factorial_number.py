#%%
def find_factorial_value(num):
    return 1 if(num==1 or num==0) else num*find_factorial_value(num-1);

given_number=10
print("factorial of " ,given_number ,"is",find_factorial_value(given_number))

#%%
number=int(input("Enter your number :"))
factorial=1
if(number<0):
    print("factorial does not exist")
elif(number==0):
    print("Factorial 0 is 1")
else:
    for i in range(1,number+1):
        factorial=factorial*i
    print("Result is ",factorial)
#%%
import math
number=int(input("Enter your number :"))
print("Result is ",math.factorial(number))
