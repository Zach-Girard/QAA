#!/usr/bin/env python



import argparse

def get_args():
    parser = argparse.ArgumentParser(description="A program used to determine the number of mapped and unmapped reads in a SAM file (No Headers).")
    parser.add_argument("-f", "--filename", help="The name of fasta file to investigate", required=True, type=str)
   
    
    return parser.parse_args()
	
args = get_args()
file = args.filename
# Go through SAM file and count all the reads that are mapped and unmapped to the genome. Do not count reads more than once.(Only count the first mapping)
with open(file, "r") as sam:
    mapped_count = 0
    unmapped_count = 0
    for line in sam:
        lst = line.split("\t") 
        flag = int(lst[1]) # the second item in tab separated line
        if((flag & 4) != 4):
            if ((flag & 256) != 256) :
                mapped_count += 1
        else:
            if ((flag & 256) != 256) :
                unmapped_count += 1
print(f"Mapped: {mapped_count}")
print(f"Unmapped: {unmapped_count}")
