#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=8
#SBATCH --mem=16GB
#SBATCH --job-name=htseq

/usr/bin/time -v htseq-count --stranded=yes 28_4D_mbnl_S20_L008.Aligned.out.sam Mus_musculus.GRCm39.112.gtf > htseq_stranded_28_4D_mbnl_S20_L008

/usr/bin/time -v htseq-count --stranded=reverse 28_4D_mbnl_S20_L008.Aligned.out.sam Mus_musculus.GRCm39.112.gtf > htseq_reverse_28_4D_mbnl_S20_L008

/usr/bin/time -v htseq-count --stranded=yes 3_2B_control_S3_L008.Aligned.out.sam Mus_musculus.GRCm39.112.gtf > htseq_stranded_3_2B_control_S3_L008

/usr/bin/time -v htseq-count --stranded=reverse 3_2B_control_S3_L008.Aligned.out.sam Mus_musculus.GRCm39.112.gtf > htseq_reverse_3_2B_control_S3_L008