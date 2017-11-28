'''This program is used to plot chromagrams'''
import matplotlib.pyplot as plt
import librosa.display as ld
import scipy.io.wavfile as sc
import librosa.feature as lf
import librosa as lb


file_name='Training_Data_Set/rock/rock.00001.wav'
plt.figure(1)
rate,data=sc.read(file_name)
plt.figure(1)
plt.plot(data)
plt.show()
M=lf.chroma_stft(data,sr=rate,n_fft=4096,hop_length=512)
ld.specshow(M,x_axis='frames',y_axis='chroma')
plt.colorbar()
plt.title('rock_1')
plt.show()
