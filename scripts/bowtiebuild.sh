#!/bin/sh -I

############################# BATCH SCRIPT ####################################
###     FILENAME:bowtie_build.sh
###
###     PURPOSE:To make a custom index combining multiple .fa files
###
###
###     USAGE: sbatch bowtie_build.sh path/to/.fa/file basename_of_output
###
###     AUTHOR: Ella Hartenian
###     DATE: March 21, 2016
###     MODIFIED: June 6, 2017
###
###############################################################################

#SBATCH --job-name=bowtie_build
#SBATCH --partition=savio2
#SBATCH --account=co_rosalind
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=3
#SBATCH --mem=9000
#SBATCH --time=40:00:00
#SBATCH --output=bowtiebuild._%j.out
#SBATCH --error=bowtiebuild_%j.err
#SBATCH --mail-user=ehartenian@berkeley.edu
#SBATCH --mail-type=END
cd $SLURM_SUBMIT_DIR


## LOAD MODULES
module load bio/bowtie2/2.3.0

## RUN!!
bowtie2-build -f $1 $2
# -f reference fasta in, or comma separated list of fasta files for each chromosome
