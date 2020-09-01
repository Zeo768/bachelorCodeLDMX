#!/bin/sh
#SBATCH -t 00:300:00
#
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=8


module restore spytens


python modelsigma.py '500MeVAng160-180test20000Array.npy' '500MeVAng160-180test20000ArrayElist.npy' '500MeVAng160-180test20000ArrayClassifier.npy' '1000MeVAng160-180test20000Array.npy' '1000MeVAng160-180test20000ArrayElist.npy' '1000MeVAng160-180test20000ArrayClassifier.npy' '1500MeVAng160-180test20000Array.npy' '1500MeVAng160-180test20000ArrayElist.npy' '1500MeVAng160-180test20000ArrayClassifier.npy' '2000MeVAng160-180test20000Array.npy' '2000MeVAng160-180test20000ArrayElist.npy' '2000MeVAng160-180test20000ArrayClassifier.npy' '2500MeVAng160-180test20000Array.npy' '2500MeVAng160-180test20000ArrayElist.npy' '2500MeVAng160-180test20000ArrayClassifier.npy'    

