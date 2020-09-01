#!/bin/sh
#SBATCH -t 00:300:00
#
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=8


module restore spytens


python modelsigma.py '500MeVAng160-18010000ArrayRec.npy' '500MeVAng160-18010000ArrayRecElist.npy' '500MeVAng160-18010000ArrayRecClassifier.npy' '750MeVAng160-18010000ArrayRec.npy' '750MeVAng160-18010000ArrayRecElist.npy' '750MeVAng160-18010000ArrayRecClassifier.npy' '1000MeVAng160-18010000ArrayRec.npy' '1000MeVAng160-18010000ArrayRecElist.npy' '1000MeVAng160-18010000ArrayRecClassifier.npy' '1250MeVAng160-18010000ArrayRec.npy' '1250MeVAng160-18010000ArrayRecElist.npy' '1250MeVAng160-18010000ArrayRecClassifier.npy' '1500MeVAng160-18010000ArrayRec.npy' '1500MeVAng160-18010000ArrayRecElist.npy' '1500MeVAng160-18010000ArrayRecClassifier.npy' '1750MeVAng160-18010000ArrayRec.npy' '1750MeVAng160-18010000ArrayRecElist.npy' '1750MeVAng160-18010000ArrayRecClassifier.npy' '2000MeVAng160-18010000ArrayRec.npy' '2000MeVAng160-18010000ArrayRecElist.npy' '2000MeVAng160-18010000ArrayRecClassifier.npy' '2250MeVAng160-18010000ArrayRec.npy' '2250MeVAng160-18010000ArrayRecElist.npy' '2250MeVAng160-18010000ArrayRecClassifier.npy' '2500MeVAng160-18010000ArrayRec.npy' '2500MeVAng160-18010000ArrayRecElist.npy' '2500MeVAng160-18010000ArrayRecClassifier.npy' '0-3GeVAng160-180100000ArrayRecElist.npy' '0-3GeVAng160-180100000ArrayRecClassifier.npy'    

