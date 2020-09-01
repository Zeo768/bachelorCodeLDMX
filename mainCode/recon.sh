#!/bin/sh
#SBATCH -t 00:180:00
#
#SBATCH -A hep2016-1-4
#SBATCH -p hep 
#SBATCH -N 1
#SBATCH --tasks-per-node=3

/projects/hep/fs7/shared/containers/ldmx-img bash

source /projects/hep/fs7/scratch/pflorido/ldmx-singularity-reloaded/libs/ldmx-sw-install/bin/ldmx-setup-env.sh

ldmx-app recon_config_short.py 0-3GeVAng160-1801E_100000.root 0-3GeVAng160-180Rec1E_100000.root
