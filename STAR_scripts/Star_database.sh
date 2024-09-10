#!/bin/bash
#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=8
#SBATCH --mem=100GB
#SBATCH --job-name=star_database
#SBATCH --output=star_database_%j.out
#SBATCH --error=star_database_%j.err


/usr/bin/time -v STAR --runThreadN 8 \
--runMode genomeGenerate \
--genomeDir Mus_musculus.GRCm39.dna.ens112.STAR_2.7.11b \
--genomeFastaFiles Mus_musculus.GRCm39.dna_sm.primary_assembly.fa \
--sjdbGTFfile Mus_musculus.GRCm39.112.gtf

