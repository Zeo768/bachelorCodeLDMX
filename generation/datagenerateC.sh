#!/bin/sh
#SBATCH -t 00:300:00
#
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=4
#SBATCH -o 0-3GeV5mmAng170-180100000_%j.out

/projects/hep/fs7/shared/containers/ldmx-img bash

source /projects/hep/fs7/scratch/pflorido/ldmx-singularity-reloaded/libs/ldmx-sw-install/bin/ldmx-setup-env.sh

ldmx-sim 1ElectronC.mac