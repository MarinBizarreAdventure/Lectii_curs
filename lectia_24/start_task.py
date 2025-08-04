import pandas as pd 
import numpy as np 

data = {
    'state':['ohio','ohio','ohio',"nevada",'nevada'],
    'year':[2000,2001,2002,2000,2001],
    'pop':[1.5,1.7,3.6,2.4,2.9]
}
frame = pd.DataFrame(data)
frame2 = pd.DataFrame(data,columns=['year','state','pop', 'debt'], index=['A','B',"C","D",'E'])

# print(frame2)

data = np.arange(9).reshape(3,3)
frame = pd.DataFrame(data, index=['r1','r3','r2'],columns=['c1','c2','c3'])

def square(x):
    return x**2

def max_minus_min(x):
    return max(x)-min(x)
print(frame)
print(frame.sort_index(axis=1))



