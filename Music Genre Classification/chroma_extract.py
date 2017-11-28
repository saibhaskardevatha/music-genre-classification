'''This library has fucnctions to extract chromgram form stft.
Descriptions of various funcitons are :
1. Hz2Octs converts  from hertz domain to octave domain
2. chroma filter acts as filter that converts stft into chromastft
3.Chroma_stft=Chroma_filter*stft
various intermediate plots are constuced to plot intermediate steps'''

import numpy as np
import matplotlib.pyplot as plt
import librosa as lb
'''
Descriptions of libraries:
numpy: matrxi computation tool box
matplotlib is used for plotting '''

#This function converts hertz to octs.log2(frequency)/(440/60))

def hz_2_oct(frequencies):
    return np.log2((frequencies)/(440// 16))

#This chroma_filter constructs filter that fitles chroma filter out of stft
def chroma_filter(sr,n_fft):
    '''sr is sampling rate while n_fft is size of frame'''

    wts = np.zeros((12, n_fft))                                    #initializing the filter to zeros

    print "intinalized=\n",wts

    frequencies = np.linspace(0, sr, n_fft, endpoint=False)[1:]    #creating array of various frequencies sampled in DFT
    print "frequencies=\n",frequencies
    frqbins = 12* hz_2_oct(frequencies)                            #converting the freincs to repective ocatve values
    print "frequencybins=\n",frqbins

    frqbins = np.concatenate(([frqbins[0] - 1.5 * 12], frqbins))   #adding an intial lower limit to ocatve which cannot be directly computed using logarithm
    # computing the differnce betwwen succesvie bins to seprate frequencies separeted by one actave
    binwidthbins = np.concatenate((np.maximum(frqbins[1:] - frqbins[:-1], 1.0), [1]))

    print "binwidthbins=\n",binwidthbins

    #constructing by filter by applying gassiaian weights  ,around each harmonic of every chroma brand, higher freqencies have lower weigths and larger widths.
    S= np.subtract.outer(frqbins, np.arange(0,12, dtype='d')).T
    print "D=\n",S
    n_chroma2 = np.round(float(12) / 2)

    print "n_chroma2=",n_chroma2
    D = np.remainder(S + n_chroma2 + 10 *12,12) - n_chroma2

    print "D after raminder =\n",D
    wts = np.exp(-0.5 * (2 * D / np.tile(binwidthbins, (12, 1))) ** 2)

    print "wts=\n",wts

    wts *= np.tile(
        np.exp(-0.5 * (((frqbins / 12 - 5) /2) ** 2)),
        (12, 1))


    wts = np.roll(wts, -3, axis=0)

    # returning th matix of 12 Xn_fft
    return np.ascontiguousarray(wts[:, :int(1 + n_fft / 2)])  #,D,frequencies,frqbins,binwidthbins,S

''''a code to generate plots
sr=44100
n_fft=4096
F,D,Freq,oct,width,S=chroma_filter(sr,n_fft)
#print S.shape
#plt.figure(1)
#plt.plot(F[0][:])
#plt.figure(2)
#plt.plot(Freq)
#plt.figure(3)
#plt.plot(oct)
#plt.figure(4)
#plt.plot(width)
#plt.figure(5)
#plt.scatter(np.arange(4096),D[0][:])
plt.figure(1)
plt.plot(S.T)
plt.show()'''

def chroma_stft(data,sr,n_fft,hoplength):
    S=lb.stft(data,n_fft,hoplength)
    Filter=chroma_filter(sr,n_fft)
    return Filter*S
