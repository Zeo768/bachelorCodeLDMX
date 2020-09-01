#!/bin/sh
#SBATCH -t 00:60:00
#
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=4
#SBATCH -o rta2.5GeVtest_%j.out

module restore spytens

/projects/hep/fs7/shared/containers/ldmx-img bash

source /projects/hep/fs7/scratch/pflorido/ldmx-singularity-reloaded/libs/ldmx-sw-install/bin/ldmx-setup-env.sh

python RootToArray.py -i 2.5GeVTest1E_10000.root -o 2.5GeVtest10000Array
