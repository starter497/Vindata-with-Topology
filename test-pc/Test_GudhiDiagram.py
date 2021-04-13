# -*- coding: utf-8 -*-
"""
Created on March 20th

@author: cnem modified Neils original code

"""

import os

import numpy as np

import gudhi  #create complexes

import matplotlib

from PIL import Image, ImageOps

from matplotlib import pyplot as plt

import persistencecurves as pc # vectorization.  Be sure to pip install import

import pydicom #converts dicom images to PIL. Be sure to pip install import

from pydicom_PIL import show_PIL #just to show the image

import warnings

warnings.filterwarnings("ignore")

usetex = matplotlib.checkdep_usetex(True) #I dont have latex)


#--------------------- Functions -----------------

def calculate_diagram_gudhi(image):

    reshaped = np.reshape(image, [image.shape[0]*image.shape[1]], order = 'F')
    # reshapes image to a single vector

    Complex = gudhi.CubicalComplex(dimensions=image.shape, top_dimensional_cells=reshaped)
    # creates the cubical complex from the image

    Complex.persistence()

    Dgm0 = Complex.persistence_intervals_in_dimension(0)
    # compute oth dimensional persistence diagram

    Dgm1 = Complex.persistence_intervals_in_dimension(1)

    return Dgm0, Dgm1






#--------------------Configuration---------------------


path = r"/vindata/test/"

testfilename = os.listdir(path)


dir_pc = os.path.join("/vindata","test-pc")

os.mkdir(dir_pc)    #persistence curve directory

dir_im = os.path.join ("/vindata", "test-images")

os.mkdir(dir_im)    #pixel array directory




print("Number of test files:",len(testfilename))

image_dicom =  []
image = []

''' useful if you want to store everything without saving.

ALL_PD0 = []    #all of the persistent diagram information 0dimension
ALL_PD1 = []    #all of persistent diagram info 1dimension
BC0 = []       #all of betticurve 0-dim
BC1 = []       #all of betticurve 1-dim
G0 = []
G1 = []
ATL0 = []
ATL1 = []
'''

PC = []

for j in range(3):

     #remove comment if you want to make a directory for saving plots(not necessary)
    
    ID = os.path.splitext(testfilename[j])[0]
    
    '''
    results_dir = os.path.dirname(__file__)

    results_dir = os.path.join(results_dir, ID + "-pc" )

    if not os.path.isdir(results_dir):

       os.makedirs(results_dir)
    
    '''

    image_dicom.append(pydicom.dcmread(path + testfilename[j]))

    image = image_dicom[j].pixel_array

    #max_pixel = np.amax(image)

    

    # -----------------Rescaling Pixel intensity to 0-255 ---------------
    

    image = image.astype(float) # gets floating point numbers for values

    image = (np.maximum(image,0) / image.max()) * 255.0 #Rescales to grayscaled between 0-255 rather than 3000-65,535.  Too much intensity for memory

    image = np.uint8(image) 
   
    
    
   
   # print(image.shape) #Note NOT ALL IMAGES ARE SAME SIZE


   #print(image_dicom[j])  #if you want to see the meta-data

   #show_PIL(image_dicom[j]) #if you want to see the images
    

    np.save("/vindata/test-images/" +ID, image)

    [Dgm0,Dgm1] =calculate_diagram_gudhi(image)

    print(j) #tells you the progress, finish at 15,000


    
    #ALL_PD0.append(Dgm0) #This is the array for all of the persistent diagrams
    #ALL_PD1.append(Dgm1) #No need to store.
    
    




#-------------Using 0- PersistentDiagram to curve info ---------
    
   
    D0 = pc.Diagram(Dgm = Dgm0, globalmaxdeath = None, infinitedeath=None, inf_policy="keep")



    D1 = pc.Diagram(Dgm = Dgm1,globalmaxdeath = None, infinitedeath = None, inf_policy= "keep")


#---------------------0 and 1 dimensional Betti curve (number of points in Fundamental box) info ----------------------


    Betti0 = D0.normalizedBetticurve(meshstart=0,meshstop= 256 ,num_in_mesh= 256)

    Betti1 = D1.normalizedBetticurve(meshstart=0,meshstop= 256 , num_in_mesh =256)

    

#-----------------------0 and 1 dimensional Guass curve info ----------------------



    Gauss0= D0.gaussian_life(meshstart=0, meshstop= 256,num_in_mesh = 256, spread = 1)

    Gauss1= D1.gaussian_life(meshstart=0, meshstop= 256, num_in_mesh= 256, spread = 1)

       



#---------------0 and 1 dimensional average Normalized Total lifespan curve info -------


    norm_lifespan0 = D0.normalizedlifecurve(0 , 256, 256)
   
    norm_lifespan1 = D1.normalizedlifecurve(0,  256, 256)

    

    
    PC = np.concatenate((Betti0, Betti1, Gauss0, Gauss1, norm_lifespan0, norm_lifespan1))

    np.save("/vindata/test-pc/" + ID, PC)

'''
 #uncomment to plot betticurves
    
    gudhi.plot_persistence_diagram(Dgm0)

    x_1 = np.linspace(0,255,num= 256) 

    

    plt.savefig(results_dir + "/Persistence Diagram .png")
 
    plt.clf()
 
    

    plt.plot(x_1, dgm0)



    

    plt.savefig(results_dir + "/BettiCurve.png")
    
    plt.clf()
'''

 

print("Processing has finished! ")


