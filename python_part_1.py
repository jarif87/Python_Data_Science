#%%
a = 10  # integer
print(a)
b = 10.05  # float
c = 'python'  # string
d = [1, 3, 4, 6, 7, 10, 'sakib']  #list
e = {'key1' : [100, 105, 106], 'key2': 'value2'}  # dictionaries
e1 = { 'students' : ["abrar","raita", "kamal"],
     'class': "first class"}
f = (1,2,3,4)  # tuple

g={1:["bangla","english","math"],"bangla":"first_paper"}

#%%
print(a)
print(b)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(g["bangla"])

#%%
#addition
a = 5
b = 10
c = a + b
print(c)

#%%
# substruction
a = 50
b = 10
c = a - b
print(c)
#%%
# multiplication
a = 20
b = 10
c = a * b
print(c)
#%%
# division
a = 50
b = 10
c = a / b
print(int(c))
#%%
#modulus
p = 11
q = 3
r = p % q
print(r)
#%%
# exponent
a = 2
b = 3
c = a**b
print(c)
#%%
#comparison
# Greater than

a = 8
b = 9

print(b > a)
#%%
# grater than or equal to
print(a >= b)
#%%
# less than or equal to
print(a <= b)
#%%
# equal to
print(a == b)
h="m"
s="m"
print(h==s)
#%%
# NOT equal to
a = 8
b = 9
c = (a != b)
print(c)
#%%
# 1.2.3 Assignment Operators

a = 25
b = 10

# a = a + b
a += b
print(a)
#%%
a -= b  # a =  a - b
print(a)
#%%
a *= b  #a=a*b
print(a)
#%%
a /= b  
print(a)
#%%
# 1.3 Strings

string = "hello world!"
print(string)
#%%
# length
print(len(string))
#%%
# index
print(string[6])

#%%
s = [ "Our first class", "thursday", "sakib", "internt",'python', 'sakib', 'tasmia', 'hasan', 'imtiaz', 'tayem' ]
# Slicing 
string = "hello world!"
print(string[2:])
print(s[2  :])
print(string[:11])
print(string[:      4])
# from backword
print(string[-1])  # only last value
print(s[:     -2])
# interval/frequency
string = "hello world!"
print(string[: : 2])
# reverse
print(string[: :-1])
# as
print(string[1:7])
#%%

# concatanate
s = "hello world"
a = " to all of us"
s = s + a
print(s)
#%%
# capitalize
print(s.upper())
#%%
m2 = "RUHIT"
print(m2.lower())

#%%
# Skip split
s="hello world to all of us"
print(s.split("o"))
#%%
# count how many (specific)laters in sentence
print(s.count("l"))
#%%
print(s.isalnum())
# contains either numeric or alphabet
string1 = "M234onica"
print(string1.isalnum()) # True 

print(s.isdigit())
print(s.find("r"))
