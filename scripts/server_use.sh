#login
 ssh username@hpc.brc.berkeley.edu
 #enter your pw + google authenticator 6 digits

 # directories for storing files, etc
 /clusterfs/rosalind/users/
 /clusterfs/vector/scratch/
 # genome file location (masked only)
 /clusterfs/vector/referenceData/igenomes/

 # loading modules and editing a script
 module avail
 module load emacs
 emacs tophat.sh

# running a script (output files will go in current directory)
sbatch /path/to/script inputs outputs
#check status of job
squeue -u username
scancel jobnumber

# move files, from computer to server
scp filename username@dtn.brc.berkeley.edu:/location/on/server
# from server to computer
scp username@dtn.brc.berkeley.edu:/location/on/server /location_to_copy

# location for JK sorted bams
/clusterfs/rosalind/users/ehartenian/JK_RNAP3_ChIP/bowtie2
