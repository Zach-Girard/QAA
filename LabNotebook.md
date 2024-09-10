# RNA-seq Quality Assessment Assignment - Bi 623 (Summer 2024)

Samples Assigned to me:

```3_2B_control_S3_L008```  and   ``` 28_4D_mbnl_S20_L008```

Files located at: ```/projects/bgmp/shared/2017_sequencing/demultiplexed/```

```3_2B_control_S3_L008_R1_001.fastq.gz```
```3_2B_control_S3_L008_R2_001.fastq.gz```

Size:
```-rw-r-----+ 1 coonrod is.racs.pirg.bgmp 359M Aug 23  2017 3_2B_control_S3_L008_R1_001.fastq.gz```
```-rw-r-----+ 1 coonrod is.racs.pirg.bgmp 421M Aug 23  2017 3_2B_control_S3_L008_R2_001.fastq.gz```

AND

```28_4D_mbnl_S20_L008_R1_001.fastq.gz```
```28_4D_mbnl_S20_L008_R2_001.fastq.gz```

Size:
```-rw-r-----+ 1 coonrod is.racs.pirg.bgmp 647M Aug 23  2017 28_4D_mbnl_S20_L008_R1_001.fastq.gz```
```-rw-r-----+ 1 coonrod is.racs.pirg.bgmp 737M Aug 23  2017 28_4D_mbnl_S20_L008_R2_001.fastq.gz```

CANNOT MOVE, COPY, OR UNZIP THESE FILES


##

04Sep2024


## Part 1 Step 1

Need to create a conda environment and install fastqc
```conda create --name QAA```
```conda activate QAA```
```conda install bioconda::fastqc```

Version check: 
```fastqc --version```                                                 
```FastQC v0.12.1```

# Running Fastqc

command: ```fastqc /projects/bgmp/shared/2017_sequencing/demultiplexed/3_2B_control_S3_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/3_2B_control_S3_L008_R2_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R2_001.fastq.gz -o . -t 4```


Files created:

```28_4D_mbnl_S20_L008_R1_001_fastqc.html```
```28_4D_mbnl_S20_L008_R2_001_fastqc.zip```
```3_2B_control_S3_L008_R2_001_fastqc.html```
```28_4D_mbnl_S20_L008_R1_001_fastqc.zip```
```3_2B_control_S3_L008_R1_001_fastqc.html```
```3_2B_control_S3_L008_R2_001_fastqc.zip```
```28_4D_mbnl_S20_L008_R2_001_fastqc.html```
```3_2B_control_S3_L008_R1_001_fastqc.zip```

I scp'd these files to my local machine to view html files in my browser.

Per Part 1 Question 3: Also, does the runtime differ? Mem/CPU usage? If so, why?

I need to rerun the command via sbatch to time the command.

sbatch script: ```Fastqc.sh```


sbatch Fastqc.sh 
Submitted batch job 15948298

User time (seconds): 151.64
        System time (seconds): 7.79
        Percent of CPU this job got: 299%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 0:53.18
        Exit status: 0


## Part 1 Question 2

Using FastQC via the command line on Talapas, produce plots of the per-base quality score distributions for R1 and R2 reads. Also, produce plots of the per-base N content, and comment on whether or not they are consistent with the quality score plots.

Created a script ```N_Content.py`` to calculate percent N content per base and plot.


Answer: My personally produced Per Base N-Content plots show the same trend as those produced by fastqc. However, my plots have their y-axis scaled by the max value. The fastqc plots are out of 100%. This allows me to see much smaller trends that are not visible in the fastqc plots. For R2 reads, it appears as though there are extremely small non-zero counts of N's past the first base position.





## Part 1 Question 3

Run your quality score plotting script from your Demultiplexing assignment in Bi622. (Make sure you're using the "running sum" strategy!!) Describe how the FastQC quality score distribution plots compare to your own. If different, propose an explanation. Also, does the runtime differ? Mem/CPU usage? If so, why?

Answer: The FastQC quality score distribution plots reflect the same trend shown in my produced plots. The fastqc plots also show the interquartile range for each base. Fastqc produced several plots for each file within 1 minute, using 300% of CPU given. Just producing 1 plot for each file using my Demultiplexing script took 7 minutes, using 98% of the CPU given(same as fastqc). The large difference in runtime is due to the level of coding using, the language used, and programs used to produce the plots.





## Creating my own plots

Copied my FirstAssignment.py script and bioinfo.py module to QAA directory. Removed any function or histogram for Indexes, and left only those for the forward and reverse reads.

Put my FirstAssignment.py in script ```my_plots.sh``` to sbatch for timing comparison.

Installed python via ```conda install python``` to QAA environment
```python --version```
```Python 3.12.5```


Installed matplotlib via ```conda install conda-forge::matplotlib``` to QAA environment
```
conda list matplotlib
# packages in environment at /projects/bgmp/zgirard/miniforge3/envs/QAA:
#
# Name                    Version                   Build  Channel
matplotlib                3.9.2           py312h7900ff3_0    conda-forge
```


For the 3_2B_control_S3_L008_R1_001 and 3_2B_control_S3_L008_R2_001 files:
sbatch my_plots.sh 
Submitted batch job 15949431
Command being timed: "./FirstAssignment.py -r1 /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R1
_001.fastq.gz -r4 /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R2_001.fastq.gz"
        User time (seconds): 424.91
        System time (seconds): 0.21
        Percent of CPU this job got: 98%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 7:11.22
        Exit status: 0


For the 28_4D_mbnl_S20_L008_R1_001 and 28_4D_mbnl_S20_L008_R2_001 files:
sbatch my_plots.sh 
Submitted batch job 15949914
ommand being timed: "./FirstAssignment.py -r1 /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R1_001.fastq.gz -r4 /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R2_001.fastq.gz"
        User time (seconds): 424.71
        System time (seconds): 0.22
        Percent of CPU this job got: 98%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 7:09.65
        Exit status: 0





## Part 1 Question 4

Comment on the overall data quality of your two libraries. Go beyond per-base qscore distributions. Make and justify a recommendation on whether these data are of high enough quality to use for further analysis.

Answer: I believe these data are high enough quality to use for further analysis. Looking beyond per-base qscore distributions, I can consider other statistics such as Sequences flagged as poor quality. All had 0 flagged. I can then look at sequence duplication and overrepresented sequences, none of which give me a "red x" evaluation. Per sequence GC content is also "green level" for all reads. 





## Part 2 Step 5

In your QAA environment, install cutadapt and Trimmomatic. Check your installations with:

cutadapt --version (should be 4.9)
trimmomatic -version (should be 0.39)

```conda install cutadapt```
```cutadapt --version```
```4.9```

```conda install trimmomatic```
```trimmomatic -version```
```0.39```




## Part 2 Step 6

Using cutadapt, properly trim adapter sequences from your assigned files. Be sure to read how to use cutadapt. Use default settings. What proportion of reads (both R1 and R2) were trimmed?

Answer: 
3_2B_control_S3_L008_R1_001.fastq.gz had 3.2% trimmed.
3_2B_control_S3_L008_R2_001.fastq.gz had 3.9% trimmed.
28_4D_mbnl_S20_L008_R1_001.fastq.gz had 6.0% trimmed. 
28_4D_mbnl_S20_L008_R2_001.fastq.gz had 6.8% trimmed.




## Cutadapt summaries:


cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -o trimmed_3_2B_control_S3_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/3_2B_control_S3_L008_R1_001.fastq.gz
This is cutadapt 4.9 with Python 3.12.5
Command line parameters: -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -o trimmed_3_2B_control_S3_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/3_2B_control_S3_L008_R1_001.fastq.gz
Processing single-end reads on 1 core ...
Done           00:00:46     6,873,509 reads @   6.7 µs/read;   8.90 M reads/minute
Finished in 46.396 s (6.750 µs/read; 8.89 M reads/minute).

=== Summary ===

Total reads processed:               6,873,509
Reads with adapters:                   219,477 (3.2%)
Reads written (passing filters):     6,873,509 (100.0%)

Total basepairs processed:   694,224,409 bp
Total written (filtered):    692,563,098 bp (99.8%)

=== Adapter 1 ===

Sequence: AGATCGGAAGAGCACACGTCTGAACTCCAGTCA; Type: regular 3'; Length: 33; Trimmed: 219477 times

## 

cutadapt -a AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o trimmed_3_2B_control_S3_L008_R2_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/3_2B_control_S3_L008_R2_001.fastq.gz
This is cutadapt 4.9 with Python 3.12.5
Command line parameters: -a AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o trimmed_3_2B_control_S3_L008_R2_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/3_2B_control_S3_L008_R2_001.fastq.gz
Processing single-end reads on 1 core ...
Done           00:00:50     6,873,509 reads @   7.3 µs/read;   8.19 M reads/minute
Finished in 50.378 s (7.329 µs/read; 8.19 M reads/minute).

=== Summary ===

Total reads processed:               6,873,509
Reads with adapters:                   268,119 (3.9%)
Reads written (passing filters):     6,873,509 (100.0%)

Total basepairs processed:   694,224,409 bp
Total written (filtered):    692,343,901 bp (99.7%)

=== Adapter 1 ===

Sequence: AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT; Type: regular 3'; Length: 33; Trimmed: 268119 times

##

cutadapt -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -o trimmed_28_4D_mbnl_S20_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R1_001.fastq.gz
This is cutadapt 4.9 with Python 3.12.5
Command line parameters: -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCA -o trimmed_28_4D_mbnl_S20_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R1_001.fastq.gz
Processing single-end reads on 1 core ...
Done           00:01:24    12,428,766 reads @   6.8 µs/read;   8.83 M reads/minute
Finished in 84.471 s (6.796 µs/read; 8.83 M reads/minute).

=== Summary ===

Total reads processed:              12,428,766
Reads with adapters:                   743,440 (6.0%)
Reads written (passing filters):    12,428,766 (100.0%)

Total basepairs processed: 1,255,305,366 bp
Total written (filtered):  1,245,001,943 bp (99.2%)

=== Adapter 1 ===

Sequence: AGATCGGAAGAGCACACGTCTGAACTCCAGTCA; Type: regular 3'; Length: 33; Trimmed: 743440 times

##

cutadapt -a AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o trimmed_28_4D_mbn
l_S20_L008_R2_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R2_001.fastq.gz
This is cutadapt 4.9 with Python 3.12.5
Command line parameters: -a AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT -o trimmed_28_4D_mbnl_S20_L008_R2_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/28_4D_mbnl_S20_L008_R2_001.fastq.gz
Processing single-end reads on 1 core ...
Done           00:01:29    12,428,766 reads @   7.2 µs/read;   8.29 M reads/minute
Finished in 89.996 s (7.241 µs/read; 8.29 M reads/minute).

=== Summary ===

Total reads processed:              12,428,766
Reads with adapters:                   841,389 (6.8%)
Reads written (passing filters):    12,428,766 (100.0%)

Total basepairs processed: 1,255,305,366 bp
Total written (filtered):  1,244,645,291 bp (99.2%)

=== Adapter 1 ===

Sequence: AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT; Type: regular 3'; Length: 33; Trimmed: 841389 times


## 

Try to determine what the adapters are on your own.

Answer: My fastqc plots show adapter content of the universal Illumina adpaters. I googled Illumina adapters and found a manual with adapter sequences. I clicked on the Truseq link first and found info on adapter trimming. I grepped for the adapters (see below). I repeated this for the AmpliSeq and Nextera, Illumina Prep, and Illumina PCR Kits adapters as well, but was not able to locate these adapters. 

From Illumina Truseq website:
IDT for Illumina–TruSeq DNA and RNA UD Indexes
The IDT for Illumina TruSeq unique dual (UD) index adapters are arranged in the plate to enforce the recommended pairing strategy.
A-tailing is performed before adapter ligation. For example, the additional A base is in parentheses in the i7 adapter, as follows.
Index 1 (i7) Adapters
(A)GATCGGAAGAGCACACGTCTGAACTCCAGTCAC[i7]ATCTCGTATGCCGTCTTCTGCTTG
OpenAdapter Trimming
The following sequences are used for adapter trimming.
Read 1
AGATCGGAAGAGCACACGTCTGAACTCCAGTCA
Read 2
AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT



Sanity check: Use your Unix skills to search for the adapter sequences in your datasets and confirm the expected sequence orientations. Report the commands you used, the reasoning behind them, and how you confirmed the adapter sequences.

Answer: The following command allow me to search for lines with the adapter sequences. I then followed up with a wc -l to count the number of lines with the adapters. I did the same with the other Illumina adapters found on their website. 

```zcat 3_2B_control_S3_L008_R1_001.fastq.gz | grep -e "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"```
```zcat 3_2B_control_S3_L008_R2_001.fastq.gz | grep -e "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"```
```zcat 28_4D_mbnl_S20_L008_R1_001.fastq.gz | grep -e "AGATCGGAAGAGCACACGTCTGAACTCCAGTCA"```
```zcat 28_4D_mbnl_S20_L008_R2_001.fastq.gz | grep -e "AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGT"```





## Trimmomatic 

Use Trimmomatic to quality trim your reads. Specify the following, in this order:

LEADING: quality of 3
TRAILING: quality of 3
SLIDING WINDOW: window size of 5 and required quality of 15
MINLENGTH: 35 bases
Be sure to output compressed files and clear out any intermediate files.


```trimmomatic PE trimmed_28_4D_mbnl_S20_L008_R1_001.fastq.gz trimmed_28_4D_mbnl_S20_L008_R2_001.fastq.gz 28_4D_mbnl_S20_L008_R1_001_forward_paired.fq.gz 28_4D_mbnl_S20_L008_R1_001_forward_unpaired.fq.gz 28_4D_mbnl_S20_L008_R2_001_reverse_paired.fq.gz 28_4D_mbnl_S20_L008_R2_001_reverse_unpaired.fq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35```
Output:
TrimmomaticPE: Started with arguments:
 trimmed_28_4D_mbnl_S20_L008_R1_001.fastq.gz trimmed_28_4D_mbnl_S20_L008_R2_001.fastq.gz 28_4D_mbnl_S20_L008_R1_001_forward_paired.fq.gz 28_4D_mbnl_S20_L008_R1_001_forward_unpaired.fq.gz 28_4D_mbnl_S20_L008_R2_001_reverse_paired.fq.gz 28_4D_mbnl_S20_L008_R2_001_reverse_unpaired.fq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35
Quality encoding detected as phred33
Input Read Pairs: 12428766 Both Surviving: 11725400 (94.34%) Forward Only Surviving: 677662 (5.45%) Reverse Only Surviving: 8727 (0.07%) Dropped: 16977 (0.14%)
TrimmomaticPE: Completed successfully

```trimmomatic PE trimmed_3_2B_control_S3_L008_R1_001.fastq.gz trimmed_3_2B_control_S3_L008_R2_001.fastq.gz 3_2B_control_S3_L008_R1_001_forward_paired.fq.gz 3_2B_control_S3_L008_R1_001_forward_unpaired.fq.gz 3_2B_control_S3_L008_R2_001_reverse_paired.fq.gz 3_2B_control_S3_L008_R2_001_reverse_unpaired.fq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35```
Output:
TrimmomaticPE: Started with arguments:
 trimmed_3_2B_control_S3_L008_R1_001.fastq.gz trimmed_3_2B_control_S3_L008_R2_001.fastq.gz 3_2B_control_S3_L008_R1_001_forward_paired.fq.gz 3_2B_control_S3_L008_R1_001_forward_unpaired.fq.gz 3_2B_control_S3_L008_R2_001_reverse_paired.fq.gz 3_2B_control_S3_L008_R2_001_reverse_unpaired.fq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:5:15 MINLEN:35
Quality encoding detected as phred33
Input Read Pairs: 6873509 Both Surviving: 6428019 (93.52%) Forward Only Surviving: 436824 (6.36%) Reverse Only Surviving: 4648 (0.07%) Dropped: 4018 (0.06%)
TrimmomaticPE: Completed successfully
##

# Plot Trimmed Reads

Plot the trimmed read length distributions for both R1 and R2 reads (on the same plot - yes, you will have to use Python or R to plot this. See ICA4 from Bi621). You can produce 2 different plots for your 2 different RNA-seq samples. There are a number of ways you could possibly do this. One useful thing your plot should show, for example, is whether R1s are trimmed more extensively than R2s, or vice versa. Comment on whether you expect R1s and R2s to be adapter-trimmed at different rates and why.


Answer:  I would expect R2 reads to be trimmed more extensively due to the lower quality of R2 reads. R2 reads also have a higher N-content. R2 reads have also been on the sequencer long and have thus experienced higher rates of degradation.


Commands to find length counts for each read:
```zcat 3_2B_control_S3_L008_R1_001_forward_paired.fq.gz | grep -A1 "^@" | grep -v "^--" | grep -v "^@" | awk '{print(length($0))}' | sort -n > Trimmed_3_2B_control_S3_L008_R1_001_Length_distribution.txt```

```zcat 3_2B_control_S3_L008_R2_001_reverse_paired.fq.gz | grep -A1 "^@" | grep -v "^--" | grep -v "^@" | awk '{print(length($0))}' | sort -n > Trimmed_3_2B_control_S3_L008_R2_001_Length_distribution.txt```

```zcat 28_4D_mbnl_S20_L008_R1_001_forward_paired.fq.gz | grep -A1 "^@" | grep -v "^--" | grep -v "^@" | awk '{print(length($0))}' | sort -n > Trimmed_28_4D_mbnl_S20_L008_R1_001_Length_distribution.txt```

```zcat 28_4D_mbnl_S20_L008_R2_001_reverse_paired.fq.gz | grep -A1 "^@" | grep -v "^--" | grep -v "^@" | awk '{print(length($0))}' | sort -n > Trimmed_28_4D_mbnl_S20_L008_R2_001_Length_distribution.txt```


Going to make plot in R

Adding ```LengthDistributions.html``` and ```LengthDistributions.Rmd``` to QAA directory

##


# Part 3 Step 10 - Install Software

In your QAA environment, use conda to install:

star
numpy
matplotlib - already installed
htseq


```conda install star -c bioconda```
```STAR --version```
```2.7.10b``
```mamba update STAR```
```STAR --version```
```2.7.11b```



```conda install numpy```
```conda list numpy```
```
# packages in environment at /projects/bgmp/zgirard/miniforge3:
#
# Name                    Version                   Build  Channel
numpy                     2.1.1           py312h58c1407_0    conda-forge
```


```conda install htseq```
```conda list htseq```
```
conda list htseq                                                                         
# packages in environment at /projects/bgmp/zgirard/miniforge3:
#
# Name                    Version                   Build  Channel
htseq                     2.0.5           py312h8cd533b_2    bioconda
```

##

# Part 3 Step 11

Find publicly available mouse genome fasta files (Ensemble release 112) and generate an alignment database from them. Align the reads to your mouse genomic database using a splice-aware aligner. Use the settings specified in PS8 from Bi621.


Created new directory in QAA called mouse to contain my Ensemble file

Used wget to retrieve assembly.
```wget https://ftp.ensembl.org/pub/release-112/fasta/mus_musculus/dna/Mus_musculus.GRCm39.dna_sm.primary_assembly.fa.gz```

And the GTF file
```wget https://ftp.ensembl.org/pub/release-112/gtf/mus_musculus/Mus_musculus.GRCm39.112.gtf.gz```

unzipped both files


Copied my Star database and alignment scripts from my PS8 directory


Entered new mouse info for star database script


batch Star_database.sh 
Submitted batch job 15989551
Command being timed: "STAR --runThreadN 8 --runMode genomeGenerate --genomeDir Mus_musculus.GRCm39.dna.ens112.STAR_2.7.11b --genomeFastaFile
s Mus_musculus.GRCm39.dna_sm.primary_assembly.fa --sjdbGTFfile Mus_musculus.GRCm39.112.gtf"
        User time (seconds): 6160.09
        System time (seconds): 68.81
        Percent of CPU this job got: 530%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 19:35.04
        Exit status: 0


Running star align 



sbatch Star_align.sh 
Submitted batch job 15990039
/projects/bgmp/zgirard/miniforge3/envs/QAA/bin/STAR-avx2 --runThreadN 8 --runMode alignReads --outFilterMultimapNmax 3 --outSAMunmapped Within KeepPairs --alignIntronMax 1000000 --alignMatesGapMax 1000000 --readFilesCommand zcat --readFilesIn ../3_2B_control_S3_L008_R1_001_forward_paired.fq.gz ../3_2B_control_S3_L008_R2_001_reverse_paired.fq.gz --genomeDir Mus_musculus.GRCm39.dna.ens112.STAR_2.7.11b --outFileNamePrefix 3_2B_control_S3_L008.
        STAR version: 2.7.11b   compiled: 2024-07-03T14:39:20+0000 :/opt/conda/conda-bld/star_1720017372352/work/source
Sep 05 18:30:26 ..... started STAR run
Sep 05 18:30:26 ..... loading genome
Sep 05 18:30:39 ..... started mapping
Sep 05 18:31:43 ..... finished mapping
Sep 05 18:31:43 ..... finished successfully
        Command being timed: "STAR --runThreadN 8 --runMode alignReads --outFilterMultimapNmax 3 --outSAMunmapped Within KeepPairs --alignIntronMax 1000000 --alignMatesGapMax 1000000 --readFilesCommand zcat --readFilesIn ../3_2B_control_S3_L008_R1_001_forward_paired.fq.gz ../3_2B_control_S3_L008_R2_001_reverse_paired.fq.gz --genomeDir Mus_musculus.GRCm39.dna.ens112.STAR_2.7.11b --outFileNamePrefix 3_2B_control_S3_L008."
        User time (seconds): 457.08
        System time (seconds): 11.68
        Percent of CPU this job got: 604%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 1:17.54
        Exit status: 0


sbatch Star_align.sh 
Submitted batch job 15990046
/projects/bgmp/zgirard/miniforge3/envs/QAA/bin/STAR-avx2 --runThreadN 8 --runMode alignReads --outFilterMultimapNmax 3 --outSAMunmapped With
in KeepPairs --alignIntronMax 1000000 --alignMatesGapMax 1000000 --readFilesCommand zcat --readFilesIn ../28_4D_mbnl_S20_L008_R1_001_forward_paired.
fq.gz ../28_4D_mbnl_S20_L008_R2_001_reverse_paired.fq.gz --genomeDir Mus_musculus.GRCm39.dna.ens112.STAR_2.7.11b --outFileNamePrefix 28_4D_mbnl_S20_
L008.
        STAR version: 2.7.11b   compiled: 2024-07-03T14:39:20+0000 :/opt/conda/conda-bld/star_1720017372352/work/source
Sep 05 18:42:56 ..... started STAR run
Sep 05 18:42:56 ..... loading genome
Sep 05 18:43:07 ..... started mapping
Sep 05 18:45:00 ..... finished mapping
Sep 05 18:45:00 ..... finished successfully
        Command being timed: "STAR --runThreadN 8 --runMode alignReads --outFilterMultimapNmax 3 --outSAMunmapped Within KeepPairs --alignIntronMax 
1000000 --alignMatesGapMax 1000000 --readFilesCommand zcat --readFilesIn ../28_4D_mbnl_S20_L008_R1_001_forward_paired.fq.gz ../28_4D_mbnl_S20_L008_R
2_001_reverse_paired.fq.gz --genomeDir Mus_musculus.GRCm39.dna.ens112.STAR_2.7.11b --outFileNamePrefix 28_4D_mbnl_S20_L008."
        User time (seconds): 829.52
        System time (seconds): 13.49
        Percent of CPU this job got: 675%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 2:04.81
        Exit status: 0




# Part 3 Step 12
Using your script from PS8 in Bi621, report the number of mapped and unmapped reads from each of your 2 sam files. Make sure that your script is looking at the bitwise flag to determine if reads are primary or secondary mapping (update/fix your script if necessary).

Copied my PS8.py script to mouse directory

Removed headers from sam files to use PS8.py
```grep -v "^@" 28_4D_mbnl_S20_L008.Aligned.out.sam > NoHeaders_28_4D_mbnl_S20_L008.Aligned.out.sam ```
```grep -v "^@" 3_2B_control_S3_L008.Aligned.out.sam > NoHeaders_3_2B_control_S3_L008.Aligned.out.sam```

```./PS8.py -f NoHeaders_28_4D_mbnl_S20_L008.Aligned.out.sam ```
```Mapped: 22657642```
```Unmapped: 793158```


```./PS8.py -f NoHeaders_3_2B_control_S3_L008.Aligned.out.sam ```
```Mapped: 12359963```
```Unmapped: 496075```

# Part 3 Step 13

06Sep2024


Count reads that map to features using htseq-count. You should run htseq-count twice: once with --stranded=yes and again with --stranded=reverse. Use default parameters otherwise.

```htseq-count --stranded=yes 28_4D_mbnl_S20_L008.Aligned.out.sam Mus_musculus.GRCm39.112.gtf > htseq_stranded_28_4D_mbnl_S20_L008```

```htseq-count --stranded=reverse 28_4D_mbnl_S20_L008.Aligned.out.sam Mus_musculus.GRCm39.112.gtf > htseq_reverse_28_4D_mbnl_S20_L008```

```htseq-count --stranded=yes 3_2B_control_S3_L008.Aligned.out.sam Mus_musculus.GRCm39.112.gtf > htseq_stranded_3_2B_control_S3_L008```

```htseq-count --stranded=reverse 3_2B_control_S3_L008.Aligned.out.sam Mus_musculus.GRCm39.112.gtf > htseq_reverse_3_2B_control_S3_L008```



# Part 3 Step 14

Demonstrate convincingly whether or not the data are from "strand-specific" RNA-Seq libraries. Include any comands/scripts used. Briefly describe your evidence, using quantitative statements (e.g. "I propose that these data are/are not strand-specific, because X% of the reads are y, as opposed to z.").

Answer: I propose the library that these data are not strand-specific, because 42.6% and 82.7% of reads in the stranded=reverse htseq-count data is mapped to genes, as opposed to 1.79% and 3.5% in the stranded=yes htseq-count data. 


```cat htseq_stranded_3_2B_control_S3_L008 | grep -v "^__" | awk '{sum += $2} END {print sum}'```
Mapped: ```221658```
```cat htseq_stranded_3_2B_control_S3_L008 | awk '{sum += $2} END {print sum}'```
Total: ```12359963```
Proportion: ```0.0179```


```cat htseq_reverse_3_2B_control_S3_L008 | grep -v "^__" | awk '{sum += $2} END {print sum}'```
Mapped: ```5260168```
```cat htseq_reverse_3_2B_control_S3_L008 | awk '{sum += $2} END {print sum}'```
Total: ```12359963```
Proportion: ```0.426```



```cat htseq_stranded_28_4D_mbnl_S20_L008 | grep -v "^__" | awk '{sum += $2} END {print sum}'```
Mapped:```411314```
```cat htseq_stranded_28_4D_mbnl_S20_L008 | awk '{sum += $2} END {print sum}'```
Total: ```11725400```
Proportion: ```0.035```


```cat htseq_reverse_28_4D_mbnl_S20_L008 | grep -v "^__" | awk '{sum += $2} END {print sum}'```
Mapped: ```9700357```
```cat htseq_reverse_28_4D_mbnl_S20_L008 | awk '{sum += $2} END {print sum}'```
Total: ```11725400```
Proportion: ```0.827```
