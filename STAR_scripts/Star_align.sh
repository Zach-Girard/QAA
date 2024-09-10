#!/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=8
#SBATCH --mem=100GB
#SBATCH --job-name=Star_alignment


/usr/bin/time -v STAR --runThreadN 8 \
--runMode alignReads \
--outFilterMultimapNmax 3 \
--outSAMunmapped Within KeepPairs \
--alignIntronMax 1000000 --alignMatesGapMax 1000000 \
--readFilesCommand zcat \
--readFilesIn ../28_4D_mbnl_S20_L008_R1_001_forward_paired.fq.gz ../28_4D_mbnl_S20_L008_R2_001_reverse_paired.fq.gz \
--genomeDir Mus_musculus.GRCm39.dna.ens112.STAR_2.7.11b \
--outFileNamePrefix 28_4D_mbnl_S20_L008.
