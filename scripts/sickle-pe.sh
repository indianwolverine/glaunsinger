#!/bin/sh -I

############################# BATCH SCRIPT ############################################################
###
###     USAGE: sbatch sickle-pe.sh [input paired-read file 1] [input paired-read file 2] [output file]
###
###     AUTHOR: Aditya Srivastava
###     DATE: July 16th, 2018
###     MODIFIED:
###
######################################################################################################


#SBATCH --job-name=sickle-pe
#SBATCH --partition=savio
#SBATCH --account=co_rosalind
#SBATCH --qos=rosalind_savio_normal
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=20
#SBATCH --mem=6000
#SBATCH --time=100:00:00
#SBATCH --output=sickle_pe_%j.out
#SBATCH --error=sickle_pe_%j.err
#SBATCH --mail-user=aditya.srivastava@berkeley.edu
#SBATCH --mail-type=END

module load sickle/1.33

sickle pe -f $1 -r $2 -t sanger -o trmd_$1 -p trmd_$2 -s $3  
