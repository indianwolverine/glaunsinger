#!/bin/sh -I

############################# BATCH SCRIPT ####################################
###     FILENAME:bowtie-build-index.sh
###
###     PURPOSE:To make a custom index combining multiple .fa files
###
###     USAGE: sbatch bowtie-build-index.sh [fasta file or comma separated list of fasta files] [output file basename]
###
###     AUTHOR: Aditya Srivastava
###     DATE: July 16th, 2018
###     MODIFIED: July 16th, 2018
###
###############################################################################

#SBATCH --job-name=bowtie-build-index
#SBATCH --partition=savio
#SBATCH --account=co_rosalind
#SBATCH --qos=rosalind_savio_normal
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=20
#SBATCH --mem=64000
#SBATCH --time=100:00:00
#SBATCH --output=bowtie_build_index_%j.out
#SBATCH --error=bowtie_build_index_%j.err
#SBATCH --mail-user=aditya.srivastava@berkeley.edu
#SBATCH --mail-type=END


## LOAD MODULES
module load bio/bowtie2/2.3.0

## RUN!!
bowtie2-build -f $1 $2
# -f reference fasta in, or comma separated list of fasta files for each chromosome
