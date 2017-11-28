import sklearn.svm as svm
import numpy as np
import pandas as pd
import csv
import librosa.display as ld
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score


#fp=open('corrcoef_extra.csv','wb')
#write=csv.writer(fp)

file_name='Chroma_Features_wide.csv'
df=pd.read_csv(file_name,delimiter=',',header=None)
mapping={'classical':0,'jazz':0,'metal':0,'rock':1}
df=df.replace({0:mapping})
feature=df[:][range(1,25)]
type=df[:][0]


#dum=pd.get_dummies(type,columns=[0])

file_name='Chroma_Features_wide_t.csv'
df_t=pd.read_csv(file_name,delimiter=',',header=None)

df_t=df_t.replace({0:mapping})
feature_t=df_t[:][range(1,25)]
type_t=df_t[:][0]


#label=type.applymap(lambda s: mapping[s])
#print label
#print type[:][0].replace(['classical'],[1],inplace=True)

X_t=pd.DataFrame.as_matrix(feature_t)
Y_t=np.array(type_t)

X=pd.DataFrame.as_matrix(feature)
Y=np.array(type)
print X.shape,Y.shape,X_t.shape,Y_t.shape
#print X_t.shape,Y_t.shape,X.shape,Y.shape
#ld.specshow(np.cov(X.T))
#M=np.corrcoef(X.T)
#write.writerows(M)
#fp.close()

plt.show()
clf=svm.SVC(kernel='rbf',C=5)
score=cross_val_score(clf,X,Y)
print score



