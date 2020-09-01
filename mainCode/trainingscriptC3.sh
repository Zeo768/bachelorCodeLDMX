#!/bin/sh
#SBATCH -t 00:900:00
#
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=10
#SBATCH -o CE0-3A160-180fixNSC208M2C104M2D0.1N5150010.00120128_%j.out

name='CE0-3A160-180fixNSC208M2C104M2D0.1N5150010.00120128'

module restore spytens

python TrainEnergyNetworkC2.py '0-3GeVAng160-180100000Array.npy' '0-3GeVAng160-180100000ArrayClassifier.npy' ${name}
