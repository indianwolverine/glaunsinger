#!/bin/sh -I

############################# BATCH SCRIPT ####################################
###
###     FILENAME:indexbam.sh
###
###     PURPOSE:To align RNAPIII ChIP seq reads to the mouse genome
###
###     USAGE: sbatch indexbam.sh [input sorted bam file] 
###
###     AUTHOR: Aditya Srivastava
###     DATE: July 17th, 2018
###     MODIFIED: July 17th, 2018
###
###############################################################################

#SBATCH --job-name=indexbam
#SBATCH --partition=savio
#SBATCH --account=co_rosalind
#SBATCH --qos=rosalind_savio_normal
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=20
#SBATCH --mem=64000
#SBATCH --time=100:00:00
#SBATCH --output=indexbam_%j.out
#SBATCH --error=indexbam_%j.err
#SBATCH --mail-user=aditya.srivastava@berkeley.edu
#SBATCH --mail-type=END

## SET VARIABLES


## LOAD MODULES
module load samtools/1.8


## RUN
samtools index $1








