#!/bin/sh -I

############################# BATCH SCRIPT ####################################
###
###     FILENAME:bowtie-align.sh
###
###     PURPOSE:To align RNAPIII ChIP seq reads to the mouse genome
###
###     USAGE: sbatch bowtie-align.sh [indexed ref genome dir] [fastq file]
###
###     AUTHOR: Aditya Srivastava
###     DATE: July 17th, 2018
###     MODIFIED: July 17th, 2018
###
###############################################################################

#SBATCH --job-name=bowtie-align
#SBATCH --partition=savio
#SBATCH --account=co_rosalind
#SBATCH --qos=rosalind_savio_normal
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=20
#SBATCH --mem=64000
#SBATCH --time=100:00:00
#SBATCH --output=bowtie_align_%j.out
#SBATCH --error=bowtie_align_%j.err
#SBATCH --mail-user=aditya.srivastava@berkeley.edu
#SBATCH --mail-type=END

## SET VARIABLES
name=$2.sam

## LOAD MODULES
module load bowtie2/2.3.4.1
module load samtools/1.8

## RUN
bowtie2 -x $1 -U $2 -S $name