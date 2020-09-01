#!/bin/sh
#SBATCH -t 00:300:00
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=10
#SBATCH -o DCE0-3A160-180fixNSD0.04N551210.0000110128_%j.out

name='DCE0-3A160-180fixNSD0.04N551210.0000110128'

module restore spytens

python TrainEnergyNetworkDNNC.py '0-3GeVAng160-180100000Array.npy' '0-3GeVAng160-180100000ArrayClassifier.npy' ${name}
