#!/bin/sh -I

############################# BATCH SCRIPT ####################################
###
###     FILENAME:bowtie-align-pe.sh
###
###     PURPOSE:To align RNAPIII ChIP seq reads to the mouse genome
###
###     USAGE: sbatch bowtie-align-pe.sh [indexed ref genome dir] [fastq file1] [fastq file2]
###
###     AUTHOR: Aditya Srivastava
###     DATE: July 17th, 2018
###     MODIFIED: July 17th, 2018
###
###############################################################################

#SBATCH --job-name=bowtie-align-pe
#SBATCH --partition=savio
#SBATCH --account=co_rosalind
#SBATCH --qos=rosalind_savio_normal
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=20
#SBATCH --mem=64000
#SBATCH --time=100:00:00
#SBATCH --output=bowtie_align_pe_%j.out
#SBATCH --error=bowtie_align_pe_%j.err
#SBATCH --mail-user=aditya.srivastava@berkeley.edu
#SBATCH --mail-type=END

## SET VARIABLES
name=$2.sam

## LOAD MODULES
module load bowtie2/2.3.4.1
module load samtools/1.8

## RUN
bowtie2 -x $1 -1 $2 -2 $3 -S $name