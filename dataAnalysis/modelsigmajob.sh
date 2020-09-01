#!/bin/sh
#SBATCH -t 00:100:00
#
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=8


module restore spytens


python modelsigma.py '500MeV10000Array.npy' '500MeV10000ArrayElist.npy' '500MeV10000ArrayClassifier.npy' '750MeV10000Array.npy' '750MeV10000ArrayElist.npy' '750MeV10000ArrayClassifier.npy' '1000MeV10000Array.npy' '1000MeV10000ArrayElist.npy' '1000MeV10000ArrayClassifier.npy' '1250MeV10000Array.npy' '1250MeV10000ArrayElist.npy' '1250MeV10000ArrayClassifier.npy' '1500MeV10000Array.npy' '1500MeV10000ArrayElist.npy' '1500MeV10000ArrayClassifier.npy' '1750MeV10000Array.npy' '1750MeV10000ArrayElist.npy' '1750MeV10000ArrayClassifier.npy' '2000MeV10000Array.npy' '2000MeV10000ArrayElist.npy' '2000MeV10000ArrayClassifier.npy' '2250MeV10000Array.npy' '2250MeV10000ArrayElist.npy' '2250MeV10000ArrayClassifier.npy' '2500MeV10000Array.npy' '2500MeV10000ArrayElist.npy' '2500MeV10000ArrayClassifier.npy' '0-3GeV100000ArrayElist.npy' '0-3GeV100000ArrayClassifier.npy'    


