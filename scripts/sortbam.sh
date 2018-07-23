#!/bin/sh -I

############################# BATCH SCRIPT ####################################
###
###     FILENAME:sortbam.sh
###
###     PURPOSE:To align RNAPIII ChIP seq reads to the mouse genome
###
###     USAGE: sbatch sortbam.sh [input bam file] [output sorted bam file]
###
###     AUTHOR: Aditya Srivastava
###     DATE: July 17th, 2018
###     MODIFIED: July 17th, 2018
###
###############################################################################

#SBATCH --job-name=sortbam
#SBATCH --partition=savio
#SBATCH --account=co_rosalind
#SBATCH --qos=rosalind_savio_normal
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=20
#SBATCH --mem=64000
#SBATCH --time=100:00:00
#SBATCH --output=sortbam_%j.out
#SBATCH --error=sortbam_%j.err
#SBATCH --mail-user=aditya.srivastava@berkeley.edu
#SBATCH --mail-type=END

## SET VARIABLES


## LOAD MODULES
module load samtools/1.8


## RUN
samtools sort $1 -o $2








