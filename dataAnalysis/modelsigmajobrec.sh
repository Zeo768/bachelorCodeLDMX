#!/bin/sh
#SBATCH -t 00:300:00
#
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=8


module restore spytens


python modelsigma.py '500MeV10000ArrayRec.npy' '500MeV10000ArrayRecElist.npy' '500MeV10000ArrayRecClassifier.npy' '750MeV10000ArrayRec.npy' '750MeV10000ArrayRecElist.npy' '750MeV10000ArrayRecClassifier.npy' '1000MeV10000ArrayRec.npy' '1000MeV10000ArrayRecElist.npy' '1000MeV10000ArrayRecClassifier.npy' '1250MeV10000ArrayRec.npy' '1250MeV10000ArrayRecElist.npy' '1250MeV10000ArrayRecClassifier.npy' '1500MeV10000ArrayRec.npy' '1500MeV10000ArrayRecElist.npy' '1500MeV10000ArrayRecClassifier.npy' '1750MeV10000ArrayRec.npy' '1750MeV10000ArrayRecElist.npy' '1750MeV10000ArrayRecClassifier.npy' '2000MeV10000ArrayRec.npy' '2000MeV10000ArrayRecElist.npy' '2000MeV10000ArrayRecClassifier.npy' '2250MeV10000ArrayRec.npy' '2250MeV10000ArrayRecElist.npy' '2250MeV10000ArrayRecClassifier.npy' '2500MeV10000ArrayRec.npy' '2500MeV10000ArrayRecElist.npy' '2500MeV10000ArrayRecClassifier.npy' '0-3GeV100000ArrayRecElist.npy' '0-3GeV100000ArrayRecClassifier.npy'    


