'''This program is used to extract corerlational coeffecient matirx which can be used for analysis during classification '''


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.image as mpimg




file_name='Chroma_window.csv'                         #csv file contating the data points
df=pd.read_csv(file_name,delimiter=',',header=None)
mapping={'classical':1,'jazz':2,'metal':3,'rock':4}   #assinging numerical labels to verbal labels in  the pandas data frame
df=df.replace({0:mapping})
feature=df[:][range(1,25)]
type=df[:][0]



plt.figure(1)

X=pd.DataFrame.as_matrix(feature)                   #converting the dataframe to numpy matrix
Y=np.array(type)
print X.shape,Y.shape

M=np.corrcoef(X.T)                                 #genrating correlational coefeecient
plt.imshow(M)
plt.colorbar()                                     #plotting the matrix
plt.show()





