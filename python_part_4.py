#%%
l = [1,2,3,4,5,6,7,8]

for num in l:
    if num%2 == 0:
        print(num, " is an even number")

for num in l:
    if num%2 != 0:
        print(num, " is an odd number")

print("done")

#%%
l = []

for letter in "language":
    
    l.append(letter)
   

print(l)
#%%
l = [ letter for letter in "language"]
print(l)
#%%
l2 = [ k for k in "python" ]
print(l2)
#%%
print([ n for n in "python" ])
#%%
for m in "bangladesh":
    
    print(m)
#%%
lst = [ x**2  for x in range(2,7)]
print(lst)
#%%
lst2 = [num   for num in range(10)    if num %2 == 0 ]
print(lst2)
#%%
list3=[num for num in range(10)]
print(list3)
#%%
l2 = [ 18,15,"sakib", 24,"mash",33,28,30,25,"mushi","colince",61,43,26,"tamim"
      ,77,"riyad",41,38,59,"fizz",'sifat',43, 28, 'nizam',72, 'noshin', 39,  'yousuf' ]

n = [x   for x in l2    if isinstance(x, int)]
s = [x   for x in l2    if isinstance(x, str)]

print("String is ",s)
print("Integer value is ",n)

#%%
l3=[1,"bangla",2,"english",3,"math",4,"america",5,"england"]
q=[v for v in l3 if isinstance(v,int)]
print(q)
w=[g for g in l3 if isinstance(g,str)]
print(w)

#%%
num=[9,1,2,3,4,5,6,7,8,9,10]
lst = [num**3   for num in n     if num % 2 == 0 ]
print(lst)
#%%
mst = [ (2*m)      for m in [x**2 for x in n]       if m%2==0   ]
print(mst)
#%%
mst2 = [ m for m in ((2*x) for x in range(1,11)) if (m>5)   ]
print(mst2)
#%%
lst = [ (x+10) for x in [x**2 for x in range (1,10)]]
print(lst)
#%%
# celcius to farenheit

c = [97,98,99,100,101,102]

#print(cel)

far = [(num*(9/5) + 32) for num in c]
print(far)