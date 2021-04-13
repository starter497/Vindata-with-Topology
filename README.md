# Vindata-with-Topology

Be sure to save these files in the /vindata directory.  Once doing so be sure to install all the required imports listed in the code.  To do so, you must do
a pip install. The computer you are using should have PIP installed. To do a pip install for many of the imports here is an example command.

$pip install persistencecurves

To run the code, be sure you are using the latest python version.

For many of us, you must enter $python3 filename.py 

The code is split into a train and test python files.  in the train python file, the code will create the pixel array and persistence curves 
for 15,000 different images. There should be two directories respectively titled train-images and train-pc

For the test python files the code will create the pixel array and persistence curves for 3,000 different images.  Similarity there will be two directories 
created titled test images and test-pc.

As of now, the code will generate an a 6 row array with each row consisting of a persistence curve for 1 and 0 dimensional holes.

When downloading the zip file, be sure to unzip the three main components, Train_GudhiDiagram.py, Test_GudhiDiagram, and pydicom_PIL.py
files and move them into the /vindata/ directory.  Note you only need one pydicom_PIL.py file in the /vindata/ directory.
