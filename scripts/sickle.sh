#!/bin/sh -I

############################# BATCH SCRIPT ####################################
###
###     USAGE: sbatch sickle.sh /input/fastq.gzip  output/file/name_trimmed.fastq
###
###     AUTHOR: Ella Hartenian
###     DATE: May 30, 2017
###     MODIFIED:
###
###############################################################################

#SBATCH --job-name=sickle
#SBATCH --partition=vector
#SBATCH --qos=vector_batch
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=3
#SBATCH --mem=6000
#SBATCH --time=100:00:00
#SBATCH --output=sickle_%j.out
#SBATCH --error=sickle_%j.err
#SBATCH --mail-user=ehartenian@berkeley.edu
#SBATCH --mail-type=END


cd $SLURM_SUBMIT_DIR

## LOAD MODULES
module load sickle/1.33

## RUN!!
sickle se -f $1 -t sanger -o $2
# se = single end reads
# turns out that after 2012 Illumina used sanger reads
