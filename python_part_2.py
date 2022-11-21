#%%

my_list = [1, 2, 3, 4, 5, "Jehan", "al-amin", "mustakim", "nafi"]
print(my_list)

print(len(my_list))
#%%
# indexing and slicing
print(my_list[3])

print(my_list[ 3:7 ])
print(my_list[:  3])
#%%
# add items manually
my_list += ["class" , "monday"]
print(my_list)
# append
my_list.append("add me")
print(my_list)
#%%
l = [ 43, 28, 72, 39, 'sifat', 'yousuf', 'nizam', 'noshin'  ]
print( len(l))
#%%
# looks sequence of numbers and string
num = l[ : 4 ] #[43,28,72,39]
print(num)
#%%
# adding two values manually
num = num + [ 10, 20 ]
print(num) 
#%%
l = [ 43, 28, 72, 39, 'sifat', 'yousuf', 'nizam', 'noshin'  ]
cat = l [ 4:  ] #["sifat","yousuf","nizam","noshin","sudarshan"]
cat = cat + ['sudarshan']
print(cat)
#%%
list1 = [ 54, 72, 30, 49, 71, 83, 67, 48, 56]
# adding a new list
num2 = [ 101,102,103 ]
list2 = list1 + num2
print(list2)
#%%
# alternate way, using "extend"
list1.extend(num2)
print(list1)
#%%
# adding a new value using append 
list2.append( 100)
print(list2)
#%%
list2.append( [50, 51, 52])
print(list2)
#%%
# inserting a new value in a specific position
list2.insert(2, 10)
print(list2)
#%%
test_list=[1,2,3,4,5]
test_list.insert(2,4) #insert accept two value
print(test_list)
#%%
list2=[1,2,3,4,5,6,7,8,90,"bangla"] #pop index 2 value
list2.pop(2)
print(list2)
#%%
# remove a specific value
list2.remove(90)
print(list2)
#%%
list3=[1,2,3,4,5,6,7] #pop last index value
list3.pop()
print(list3)
#%%
# ascending order
list2=[1,3,2,6,8,9,100,11,4,8,5]
list2.sort()
print(list2)
#%%
# ascending order
test_list_2=["bangla","physics","math","degree","tamim","shakib"]
test_list_2.sort()
print(test_list_2)
#%%
#reverse
list2=[1,3,2,6,8,9,100,11,4,8,5]
list2.reverse()
print(list2)
#%%
test_list_3=["bangla","physics","math","degree","tamim","shakib"]
test_list_3.reverse()
print(test_list_3)
#%%
list2=[1,3,2,6,8,9,100,11,4,8,5]
print(max(list2))
print(min(list2))
#%%
l1 = [1,2,3]
l2 = [4,5,6]
l3 = [7,8,9]

matrix = [l1, l2, l3]

print(matrix)
# finding a column value
print(matrix[1][2])
#%%

# 1.5 Dictionaries (keys: values)
# example 01

my_dict = {"key1": "value1", "key2":"value2"}
print(my_dict)
my_dict = {"k1": 150, "k2": 14.45, "k3": "aziz", "k4":[3,7,3,8,7,3]}
print(my_dict["k1"])
#%%
#find specific value 
print(my_dict["k4"][4])
#%%
# upper
print(my_dict["k3"].upper())
#%%
# addition
my_dict["k1"] = my_dict["k1"] + 7
print(my_dict["k1"])
#%%
# substraction
print(my_dict["k1"] - 37)
#%%
#copy
my_dict = {"k1": 150, "k2": 14.45, "k3": "aziz", "k4":[3,7,3,8,7,3]}
b = my_dict.copy()
print(b)
#%%
# getting a specific value
print(my_dict.get("k4"))
#%%
# keys and values
print(my_dict.keys())
print(my_dict.values())
#%%
# example 02
# nested dictionary
d = { "k1" : { "nest_key" : { "subnest_key": 10 } } }
print(d['k1']['nest_key']['subnest_key'])
#%%
nest = { 'one': {'two' : {'three' : [1,2,3] }}}
d3 = nest['one']
print(d3)
#%%
d4 = nest['one']['two']
print(d4)
#%%
d5 = nest['one']['two']['three']
print(d5)
#%%
city1 = { "city": [ {"dhaka":["uttara", "mirpur", "banani"]} , "ctg", "syl", "raj"]}
print(city1["city"][0]["dhaka"][1])
print(city1["city"][0])
#%%
# using string

s_var = "today is our second class"

if "his" in s_var:
    print("yes, its there")
else:
    print("its not there")
    
#%%
# using list with strings

v = [ "ruhit", "sakib", "muhit"  ]

if "muhit" in v:
    print( "yes, its there")
else:
    print("no, its NOT there ")
#%%
list3 = [ 54, 76, 31, 49, 71, 85, 67, 48, 56]

if 100 in list3:
    print("okay!")
else:
    print("NOT!")
#%%
num = 0

if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("NULL")
#%%

m = int(input("input your number:\n "))
print("your given number is: ", m)

if m > 0:
    print("positive")
elif m < 0:
    print("negative")
else:
    print("neutral")
#%%


m = float(input("input your cgpa:\n"))

if m > 3.5:
    print("A+")
elif m < 3.5 and m> 3.0:
    print("A")
elif m < 3.0 and m> 2.5:
    print("B")
elif m < 2.5 and m> 2.0:
    print("C")
else:
    print("Fail")
#%%
cgpa = int(input("Please input number out of 100: "))

if cgpa >= 80:
    print("Grade is : A+")
elif cgpa in range(70,80):
    print("Grade is : A")
elif cgpa in range(60,70):
    print("Grade is : A-")
elif cgpa in range(50,60):
    print("Grade is : B")
elif cgpa in range(40,50):
    print("Grade is : B-") 
elif cgpa in range(30,40):
    print("Grade is : B-") 
else:
    print("Sorry..! Your Grade is Under Fail mark.")
    