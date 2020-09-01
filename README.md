# bachelorCodeLDMX
Code from the Bachelor thesis, neural networks applied on energy reconstruction of the LDMX ECal.
Code is mainly written in python. ROOT, Keras, Tensorflow is also needed to run the code. Code was run on the Aurora cluster at Lund University.

The code is divided into 3 parts. The generation folder is for the code that generates data sample using the LDMX Geant4 setup. 
This includes on shell script to execute which runs the 1ElectronC.mac script in a container. In the script there are different variables given that determine the shower characteristics.
The root file created is named according to EnergyAngle1E_numberOfEvents.root. 

In the mainCode folder we have the code that generates reconstructed event hits in Calorimeter aswell as code to turn the root file hits into numpy arrays that can be trained on.
Further the TrainEnergyNetwork* files are the file that trains the network with different parameters given using Keras and Tensorflow.
The trainingscript* is just the shell script for the different setup with different input files.
