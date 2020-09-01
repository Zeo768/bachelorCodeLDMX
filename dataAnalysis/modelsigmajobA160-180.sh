#!/bin/sh
#SBATCH -t 00:100:00
#
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=8


module restore spytens


python modelsigmaA160-180.py '500MeVAng160-18010000Array.npy' '500MeVAng160-18010000ArrayElist.npy' '500MeVAng160-18010000ArrayClassifier.npy' '750MeVAng160-18010000Array.npy' '750MeVAng160-18010000ArrayElist.npy' '750MeVAng160-18010000ArrayClassifier.npy' '1000MeVAng160-18010000Array.npy' '1000MeVAng160-18010000ArrayElist.npy' '1000MeVAng160-18010000ArrayClassifier.npy' '1250MeVAng160-18010000Array.npy' '1250MeVAng160-18010000ArrayElist.npy' '1250MeVAng160-18010000ArrayClassifier.npy' '1500MeVAng160-18010000Array.npy' '1500MeVAng160-18010000ArrayElist.npy' '1500MeVAng160-18010000ArrayClassifier.npy' '1750MeVAng160-18010000Array.npy' '1750MeVAng160-18010000ArrayElist.npy' '1750MeVAng160-18010000ArrayClassifier.npy' '2000MeVAng160-18010000Array.npy' '2000MeVAng160-18010000ArrayElist.npy' '2000MeVAng160-18010000ArrayClassifier.npy' '2250MeVAng160-18010000Array.npy' '2250MeVAng160-18010000ArrayElist.npy' '2250MeVAng160-18010000ArrayClassifier.npy' '2500MeVAng160-18010000Array.npy' '2500MeVAng160-18010000ArrayElist.npy' '2500MeVAng160-18010000ArrayClassifier.npy' '0-3GeVAng160-180100000ArrayElist.npy' '0-3GeVAng160-180100000ArrayClassifier.npy'    


