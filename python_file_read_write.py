f=open("E://python//test.text","x")
data="hello world"
f.write(data)
f.close()

#%%
f=open("E://python//test.text","r")
data=f.read()
print(data)
f.close()
#%%
data=[1,2,3,4,5,6]
file_open=open("E://python//mytest.text","x")
for value in data:
    record=str(value)
    file_open.write(record)
    file_open.write("\n")
    
file_open.close()

#%%
f=open("E://python//mytest.text","r")
data=f.read()
print(data)



