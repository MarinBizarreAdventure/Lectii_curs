import matplotlib.pyplot as plt
import numpy as np 
import random 

x = ["red", "yellow", "green", "blue", "pink"]
y = np.array([random.randint(1,100) for x in range(1,6)])

plt.pie(y,labels=x, shadow=True, explode=[0.2,0,0,0,0], colors=x, startangle = 175)
plt.show()
