#%%
# 4.1 Tuple

t = (1,2,3,4,5)
print(len(t))

print(t[3])
#%%

t = (1,2,3,4,5)
s = (11,12,13,14,15)

list_of_tuple = [s,t]
print(list_of_tuple)

print(list_of_tuple[0][ : 2 ])
#%%
(age, income) = "40,200000".split(",")
print(age)
print(income)
#%%
x="bangla language"
g=x.split()
print(g)
#%%
txt = "hello, my name is Peter , I am 26 years old"

x = txt.split(",")

print(x)
print("first index value =",x[0])
print("third index value =",  x[2])
#%%
txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 2)

print(x)
#%%
# unpacking tuple

m = [ (1,2), (3,4), (5,6)]

print(m[0][1])
#%%
# using loop
m = [ (1,2), (3,4), (5,6)]
for t in m:
    print(t[0])
#%%
# for loop in tuple
d = [ (23,62), (54,70) ,(14,20), (41,38)  ]

for (i,j) in d:
    i += 100
    j -= 50
    print("value of  i is =",i)
    print("value of j is =",j)
    print("End")
#%%
f=[("bangla",1),("english",2),("math",3),("physics",4),("chemistry",5)]
for m,n in f:
    print("all subject name and number is= ",m,n)
  
#%%
# for loop in dictionary
d = { 'k1':1,  'k2': 2, 'k3': 3  }

print(d)

for num in d:
    print(num)
#%%   
for (k,v) in d.items():
    print((k,v))

#%%
d = { 'k1':1,  'k2': 2, 'k3': 3  }
for (k,l) in d.items():
    
    print((k,l))
#%%
# 5.1 function

def number(x):    # name(arguement)
    return x**2

number(8)
print(number(8))
#%%
def addition(x,y):
    z=x+y
    return z
print("value is ",addition(55,4))

#%%
def square(f, h):
    return f(h)

print(square(number, 6))
#%%
#  lambda function
print(square(lambda x: x*x, 3))
#%%
minus=lambda x,y:x-y
print(minus(5,4))
#%%
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#%%
x = lambda a, b : a * b
print(x(5, 6))
#%%
test=lambda b:b+1
print(test(4))
#%%
greet = lambda : print('Hello World')
greet()
#%%
first_string=lambda :print("bangladesh is a small country with large population")
first_string()
#%%
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('riyad')
#%%
def wednesday(x, y):
    x = (x**2) + (4*x) -3
    y = (y**3) + (4*y) + 6
    z = x + y
    
    return z

print("Result is ",wednesday(3, 2))
#%%
def python(x):
    print("this is our third class")
    return

python(4)
#%%
def python(x):
    print("fourth class")
    return

#x = 1
print(python(5))

#%%
def laptop (x, y=50):
    print(x,y)
    return

laptop(5)
#%%
def wednesday(x, y):  # case 1
    y =10  # case 2: pass by value argument
    x = (x**2) + (4*x) -3
    y = (y**3) + (4*y) + 6
    z = x + y
    print(z)
    return

wednesday(3,2)
#%%
# *l mean can take multiple value=*l=12,14,15,17,20,m=1000
def mouse(m, *l):
    print(m)
    for b in l:
        print(b)
    return

mouse(1000, 12, 14, 15,17, 20)
#%%
a = [100, 120, 124, 131, 150]
def phone(x):
    x[0] = 500
    print(x)
    return

phone(a)

print(a)
#%%
# default argument

def laptop (x, y=50):
    print(x,y)
    return

laptop(5)
#%%
# pass by value argument
def pen(x):
    x= 60
    print(x)
    return

x = 1000
pen(10)

print("value of X is",x)


















