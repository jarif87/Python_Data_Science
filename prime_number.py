num=int(input("Enter your number :"))
count=0
i=1
while(i<=num):
    if num%i==0:
        count=count+1
    i=i+1
if count==2:
    print(f"{num} Number is Prime")
else:
    print(f"{num} Number is not Prime")
    
    
    
