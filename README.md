# RNA-seq Quality Assessment & Strand-Specificity Determination

Quality-control and exploratory analysis of two paired-end mouse RNA-seq libraries, comparing a custom-built QC script against industry-standard tools, then using splice-aware alignment and gene-level counting to empirically determine library strandedness.

## Overview

Given two demultiplexed, paired-end RNA-seq libraries (`3_2B_control` and `28_4D_mbnl`), this project:

1. Benchmarks a **custom Python QC script** (per-base quality score + N-content, running-sum algorithm) against **FastQC**, comparing both output and runtime/resource usage.
2. Performs **adapter and quality trimming** with `cutadapt` and `Trimmomatic`, and quantifies how much of each library was trimmed.
3. Aligns trimmed reads to the mouse genome (Ensembl GRCm39, release 112) with the **STAR** splice-aware aligner.
4. Runs **`htseq-count`** in both `stranded=yes` and `stranded=reverse` modes to determine, from first principles, whether the libraries are strand-specific.

Full write-up with all figures and tables: [`QAA_report.pdf`](QAA_report.pdf) (source: [`QAA_report.Rmd`](QAA_report.Rmd)).

## Key results

**Strandedness:** Both libraries are **reverse-stranded**. Using `htseq-count --stranded=reverse`, 42.6% and 82.7% of reads mapped to genes for the two libraries, versus only 1.8% and 3.5% under `--stranded=yes` — a >20x difference that only makes sense if the second read is sequenced from the same strand as the mRNA.

| Library | `stranded=yes` | `stranded=reverse` |
|---|---|---|
| `3_2B_control` | 1.8% mapped | 42.6% mapped |
| `28_4D_mbnl` | 3.5% mapped | 82.7% mapped |

**Custom QC script vs. FastQC:** the two agree on per-base quality and N-content trends, but the custom Python implementation took ~7 minutes per file vs. FastQC's <1 minute across all four files — a concrete illustration of why production pipelines lean on optimized, compiled/multi-threaded tools rather than pure-Python re-implementations for routine QC.

**Adapter trimming:** 3.2-6.8% of reads were removed per file, with R2 consistently trimmed at a higher rate than R1 (consistent with R2's lower base quality and higher N-content late in the read).

## Tools & skills demonstrated

`FastQC` · `cutadapt` · `Trimmomatic` · `STAR` · `htseq-count` · conda environment management · SLURM batch scripting (HPC cluster) · Python (custom QC plotting) · R / R Markdown (reproducible reporting)

## Repository layout

```
Fastqc_data/            FastQC reports + SLURM script
N_Content_data/         Custom per-base N-content script and plots
Q_Score_plots/          Custom per-base quality score script and plots
Trimmed_distributions/  Post-trim read length distribution analysis (R)
STAR_scripts/           Genome index build + alignment SLURM scripts
htseq_data/             Gene-level counts (stranded vs. reverse) + SLURM script
QAA_report.Rmd / .pdf   Full report with figures, tables, and conclusions
```
