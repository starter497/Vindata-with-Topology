import numpy as np 

import os

import gudhi  #create complexes

import matplotlib

import  time

from PIL import Image, ImageOps

from matplotlib import pyplot as plt

import persistencecurves as pc # vectorization

import warnings

warnings.filterwarnings("ignore")

usetex = matplotlib.checkdep_usetex(True) #I dont have latex)

#---------------------------- Configuration ---------------


path = "/vindata/train-pc/"

train_pc_name =os.listdir(path)



#------------------------------ Function -----------------------


for j in range(len(train_pc_name)):

    ID = os.path.splitext(train_pc_name[j])[0]  #strips extension

    Combined_Array = np.load(ID + ".npy") #loads the array

    Split_Array = np.array_split(Combined_Array,6) #unconcatenate array originally (note I concatenated 6 together and each array had equal dimension sizes)

    row_concat_arr = np.vstack((Split_Array[0],Split_ Array[1], Split_Array[2], Split_Array[3], Split_Array[4], Split_Array[5]))  
   
   #combines the curves correctly with each row indicating a curve

    print("progress:",j)

    np.save("/vindata/train-pc/"+ID,row_concat_arr) #overwrites each array correctly


# -------------------------------- Done --------------





'''#function for one specific file


ID = "0a3b8d3f979c06dc7b8ff6cf1f9343e4"

Array =np.load(ID + ".npy")
 
Array = np.array_split(Array,6)

print("Betti0:", Array[0].shape)
print("Lifespan0:", Array[1].shape)
print("Gauss0:", Array[2].shape)
print("Betti1:", Array[3].shape)
print("Lifespan1:", Array[4].shape)
print("Gauss1:", Array[5].shape)

persistent_array = np.vstack((Array[0], Array[1], Array[2], Array[3], Array[4], Array[5]))

print("persistent_arrays:", persistent_array)
print("array_size:", persistent_array.shape)
np.save(ID, persistent_array)


x = np.linspace(0,255,256)
Myplot= plt.plot(x, persistent_array[5,:])
plt.savefig("Myplot")
'''







