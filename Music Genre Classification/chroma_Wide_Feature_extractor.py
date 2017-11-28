'''This program is used to extract chromogram and its features and store them in repective csv files  features extrated are mean and varince of enrgy of each chroma over
10 frames with a hop length of 5 frames.'''

import librosa as li
import chroma_extract as lf
import numpy as np
import librosa.display as ld
import scipy.io.wavfile as sc
import matplotlib.pyplot as plt
import sklearn.svm as svm
import csv
import os
'''Library descriptions:
numpy: numerical matrix compuation library
scipy is scientific compuation libaray
csv is used for reading and manipulating csv files
os is used to work with directories and other system funcitons'''



tds=open('Chroma_window_eli_rock.csv','wb')                            #creating a new csv file to store the extracted chromogram features
tds_write=csv.writer(tds)

working_dir="C:\\Users\\deekshisth raya\\Desktop\\DSP_draft2\\converted"
geners=os.listdir(working_dir)[:-1]                                    #lists various geners in working directory
Train_files=dict()                                                     #A dictionary where key is the genere and the data is a list of all files in it
Train_files.fromkeys(geners)
for x in geners:                                                      # To make of dictionary Training data
    data=os.listdir(working_dir+'\\'+x)
    Train_files[x]=data

fig=plt.figure(1)                                                      #generating a figure to polt
feature=dict()                                                         #this contains feature vecotrs in repective genres
feature.fromkeys(geners)
for gener in geners:                                                   # This iterates in various directories over each genre


    for music in Train_files[gener]:
        final=np.empty((1,12),float)                                   #this iterates over each files in a given genre
        name=working_dir + '\\' + gener + '\\' + music
        rate,data=sc.read(name)

        #print rate,data
        if (len(data.shape) == 2):                                     # resovling  files with 2 channels.
            data = data[:,0]


        C_DFT=lf.chroma_stft(y=data,sr=rate,n_fft=4096,hop_length=2048) # this extracts chormogram from time series

        final=C_DFT.T
        lower= range(0, len(final),5)                                   #groups 10 frames with a hoplength of 5 frames

        for i in range(len(lower) - 2):
            window=final[lower[i]:lower[i+2]][:]                        #each window is set of 10frames
            #print window.shape
            centro=np.mean(window,axis=0)                               #finding mean energy in each chroma over 10frames
            #print centro.shape
            dev=np.std(window,axis=0)                                   #finding the deviation in each chroma over 10 frames
            #print dev.shape
            dev=np.reshape(dev,(1,len(dev)))
            centro=np.reshape(centro,(1,len(centro)))                   #reshaping  the vectors
            new=np.append(centro,dev,axis=1)
            tds_write.writerows(np.concatenate(([[gener]],new),axis=1))  #concatenating and forming the feature vectors along with label and writing it to csv files


tds.close()                                                               #closing the csv file

