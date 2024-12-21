
import pandas as pd
import wave
import contextlib
import os


#Reading the foldar of .wav files
path="/Users/nellygarcia/Downloads/JetSynth"
os.chdir(path)

#Reading the files in the directory
#count the number of files in the directory
c=0

for file_name in os.listdir(os.getcwd()):
    #count the number of files in the directory
    if file_name.endswith(".wav") or file_name.endswith(".aiff"):
        c+=1
        print(file_name)
        #New name for the file before the .wav
        new_name=file_name.split(".")[0]
        new_name="JetSynth-"+str(c)+"-8"+".wav"
        print("TEST",new_name)
        os.rename(file_name,new_name)
       
    else:
        print("No .wav or .aiff files in directory")
print("Number of files in the directory: ", c)   

