# bachelorCodeLDMX
Code from my Bachelor thesis, neural networks applied on energy reconstruction of the LDMX ECal.
Code is mainly written in python. ROOT, Keras, Tensorflow is also needed to run the code. Code was run on the Aurora cluster at Lund University.
Code could be made better by importing variables so that the files could be iterated inside of a shell script. Also naming conventions is not done very well, I was a bit sloppy unfortunately.

The code is divided into 3 parts. The generation folder is for the code that generates data sample using the LDMX Geant4 setup. 
The mainCode folder has code to convert from root format into numpy arrays aswell as generating reconstructed event hits. The code that trains the networks from the data array is also in this file.
The dataAnalysis folder has code that was used to analyse the data and produce plots used in the thesis.
## generation

datagenerateC.sh is a shell script to execute which runs the 1ElectronC.mac script in a container. In the script there are different variables given that determine the shower characteristics. These are defined in the general particle source(gps) documentation for Geant4.
The root file created is named according to EnergyAngle1E_numberOfEvents.root. 
## mainCode
Firstly we have the RootToArray.py rootToRecArray.py, these two files are run to convert from root files to numpy arrays containing the information needed for the neural network. This information is the energy deposits at x,y,z position aswell as the electron initial energy for that event.
Both script were run in a LDMX software container using python file.py -i inputFile.root -o outputfile

Further the TrainEnergyNetwork* files are the file that trains the network with different parameters given using Keras and Tensorflow.
DNNC ending is for training the dense neural network. C2 is for the convolutional neural networks.
The trainingscript* is just the shell script for the different setup with different input files for the two data sets.
The outputfiles are named according to a certain scheme with the commas removed: CE,Energy range,fix,C, number of Conv filters, Size of filter,M(for maxpooling),Maxpooling size,C(second layer), number of Conv filters, Size of filter,M(for maxpooling),Maxpooling size, D(for dropout), Dropout percentage,N, Number of dense layers, Number of nodes, Number of output nodes, Learning rate, Epochs, Batch size.

## dataAnalysis

Here the main part is the modelsigma python files which computes the energy resolution of the different models on data sets with certain energy. The code also computes a mean squared error and a mean absolute error for the different models. The code plots in the end the result as seen from the main result plots in the thesis.

The plot* files are just quickly written code used to visualize different parts of the data files. plotDists.py.py(excellent name...) plots x,y and z distributions of the hits in an event, plotarray.py plots the 3d distribution of an event and plotenergy.py plots the different energy values either true or the sum of the hits in the array scaled up.


// Daniel Magdalinski
