#!/bin/sh -I

############################# BATCH SCRIPT ####################################
###
###     FILENAME:bowtie2.sh
###
###     PURPOSE:To align RNAPIII ChIP seq reads to the mouse genome ( no need for splicing so
###     no need for tophat)
###
###     USAGE: sbatch bowtie2.sh identifier_name path/to.fastq
###
###     AUTHOR: Ella Hartenian
###     DATE: Sept 7, 2017
###     MODIFIED:
###
###############################################################################

#SBATCH --job-name=bowtie2
#SBATCH --partition=savio2
#SBATCH --account=co_rosalind
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=3
#SBATCH --mem=6000
#SBATCH --time=48:00:00
#SBATCH --output=bowtie2_%j.out
#SBATCH --error=bowtie2_%j.err
#SBATCH --mail-user=ehartenian@berkeley.edu
#SBATCH --mail-type=END
cd $SLURM_SUBMIT_DIR

## SET VARIABLES
name=$1_bowtie2

## MAKE DIRECTORY WHERE OUTPUT WILL GO.
## Folder will have basename of fastq file.
## mkdir $name


## LOAD MODULES
#module load tophat2/2.0.13
module load bowtie/2.2.9
module load samtools/0.1.19

## RUN!!
bowtie2 -x /clusterfs/rosalind/users/ehartenian/genome_files/Ensembl/GRCm38_unmasked/Chromosomes/GRCm38_unmask  -U $2 -S $name
