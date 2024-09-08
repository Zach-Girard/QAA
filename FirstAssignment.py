#!/usr/bin/env python

import bioinfo

import argparse

# arguments to pass file names
def get_args():
    parser = argparse.ArgumentParser(description="A program used to calculate and plot the mean quality score per base position.")
    parser.add_argument("-r1", "--ForwardRead", help="The name of the R1 fastq file.", required=True, type=str)
    parser.add_argument("-r4", "--ReverseRead", help="The name of the R2 fastq file.", required=True, type=str)
    return parser.parse_args()
	
args = get_args()






Read1 = args.ForwardRead


# Initialize function for sequence read quality scores
import copy
def init_list101(lst: list, value: float=0.0) -> list:
    '''This function takes an empty list and will populate it with
    the value passed in "value". If no value is passed, initializes list
    with 101 values of 0.0.'''
    for i in range(101):
        new_value = copy.copy(value)
        lst.append(new_value)
    return lst   


# Initialize list for forward reads
Read1_list = []
init_list101(Read1_list)


# Read forward read file and sum the quality scores for each base position
import gzip
counter = 0
with gzip.open(Read1, 'rt') as fh:
    for line in fh:
        line = line.strip()
        counter += 1
        if counter%4 == 0:
            index = 0
            for phred_score in line:
                Read1_list[index] += bioinfo.convert_phred(phred_score) # type: ignore
                index += 1 



# Take the sum in each position and calculate the mean
index = 0
for sum in Read1_list:
    Read1_list[index] = sum/ (counter / 4)
    index += 1






Read2 = args.ReverseRead

# Initialize list for reverse reads
Read2_list = []
init_list101(Read2_list)

# Read reverse read file and sum the quality scores for each base position
counter = 0
with gzip.open(Read2, 'rt') as fh:
    for line in fh:
        line = line.strip()
        counter += 1
        if counter%4 == 0:
            index = 0
            for phred_score in line:
                Read2_list[index] += bioinfo.convert_phred(phred_score) # type: ignore
                index += 1 

# Take the sum in each position and calculate the mean
index = 0
for sum in Read2_list:
    Read2_list[index] = sum/ (counter / 4)
    index += 1





# Histograms for mean quality scores per base position

import matplotlib.pyplot as plt # type: ignore

# Plot for the forward read
plt.plot(Read1_list, color = "red")
plt.title("Mean Quality Score per Base - Forward Read")
plt.xlabel("Base Position")
plt.ylabel("Mean Quality Score")
plt.ylim(0,41)
plt.savefig("28_4D_mbnl_S20_L008_R1_001.png")
plt.close()


# Plot for the reverse read
plt.plot(Read2_list, color = "red")
plt.title("Mean Quality Score per Base - Reverse Read")
plt.xlabel("Base Position")
plt.ylabel("Mean Quality Score")
plt.ylim(0,41)
plt.savefig("28_4D_mbnl_S20_L008_R2_001.png")
plt.close()



