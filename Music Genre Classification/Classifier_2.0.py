'''This Program is used to run SVM and MLP classifier on the the data points processed from the o
other programs that extracts features from chromagram'''

import sklearn.svm as svm
import numpy as np
import pandas as pd
import csv
import librosa.display as ld
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.neural_network import MLPClassifier
import sklearn.preprocessing as skp

'''Descriptions of libraries:
1.numpy is matrix computation toolbox for python
2.pandas is a dataanlysis toolbox
3.csv is used to read and write csv files
4.librosa.display is used to plot figure
5.sklearn is  scikit machine learning toolbox that has been used for making SVM and MLP classifier(Multilayer perceptron )'''

file_name='Chroma_window_Mfcc.csv'                    # csv file which has required feature vectors
df=pd.read_csv(file_name,delimiter=',',header=None)   #reading the csv file
mapping={'classical':1,'jazz':2,'metal':3,'rock':4}   #giving numerical labels to four different genre classes under inspection
df=df.replace({0:mapping})                            #replacing labels in dataframe with numrical labels
feature=df[:][range(1,30)]                            #slicing dataframe to make feature  vectores
type=df[:][0]                                         #extracting labels of each feature vector









X=pd.DataFrame.as_matrix(feature)    #converting into numpy array
Y=np.array(type)
print X.shape,Y.shape
'''the below comments can be used for debugging and to extract covarince matrix for inspection '''
#print X_t.shape,Y_t.shape,X.shape,Y.shape
#ld.specshow(np.cov(X.T))
#M=np.corrcoef(X.T)
#write.writerows(M)
#fp.close()
#plt.show()
X_N=skp.normalize(X,axis=0)        #it is used to normalize the data that shall be later passed to the classifier
#print X_N.shape

#use the svm code to run the SVM classifer and can make cahanges to the svm model dependin on C values
#C values can be used to overfit the data
'''clf=svm.SVC(kernel='rbf',C=5)
score=cross_val_score(clf,X,Y)
print score'''
#use the below code to run Multilayer perceptron
clf=MLPClassifier(solver='lbfgs',hidden_layer_sizes=(20,12,12))
score=cross_val_score(clf,X_N,Y)
print score



