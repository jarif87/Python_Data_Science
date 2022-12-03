import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8]
y=[2,10,44,50,6,7,8,9]
plt.plot(x,y)
plt.xlabel("Time\n",fontsize=15,color="black")
plt.ylabel("Temperature\n",fontsize=15,color="blue")
plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np
x=[0,1,2,3,4,5,6,7]
y=np.sin(x)
z=y
print(z)
plt.plot(x,y)
plt.xlabel("\nNumber",fontsize=15,color="black")
plt.ylabel("Sin_Value\n",fontsize=15,color="orange")
plt.show()
#%%
import matplotlib.pyplot as plt
import numpy as np
x_start=0
x_stop=2*np.pi
increment=0.1
x=np.arange(x_start,x_stop,increment)
y=np.sin(x)
plt.plot(x,y)
plt.xlabel("From Start",fontsize=15,color="blue")
plt.ylabel("Sin Value\n",fontsize=15,color="black")
plt.show()
print(x_stop)

#%%





























