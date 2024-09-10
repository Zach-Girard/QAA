#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=8
#SBATCH --mem=16GB
#SBATCH --job-name=fastqc



/usr/bin/time -v fastqc /projects/bgmp/shared/2017_sequencing/demultiplexed/3_2B_control_S3_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/3_2B_control_S3_L008_R2_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R2_001.fastq.gz -o . -t 4