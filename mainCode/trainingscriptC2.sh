#!/bin/sh
#SBATCH -t 00:900:00
#
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=10
#SBATCH -o CE0-3fixC208M2C104M2D0.1N5150010.00120256_%j.out

name='CE0-3fixC208M2C104M2D0.1N5150010.00120256x2'

module restore spytens

python TrainEnergyNetworkC2.py '0-3GeV100000Array.npy' '0-3GeV100000ArrayClassifier.npy' ${name}
