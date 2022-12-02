number=int(input("Enter your value :"))
num1,num2=0,1
sum=0
if number<=0:
    print("Number is Greater than Zero")
else:
    for i in range(0,number):
        print("Fibonacci number is",sum)
        num1=num2
        num2=sum
        sum=num1+num2
#%%


# Function for nth Fibonacci number
 
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 
print(Fibonacci(10))
















