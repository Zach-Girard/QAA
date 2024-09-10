#!/usr/bin/env python


import argparse

# arguments to pass file names
def get_args():
    parser = argparse.ArgumentParser(description="A program used to calculate and plot the N content per base position.")
    parser.add_argument("-f", "--file", help="The name of the fastq file.", required=True, type=str)
    
    return parser.parse_args()
	
args = get_args()



file = args.file



import copy

def init_list(lst: list, value: float=0.0) -> list:
    '''This function takes an empty list and will populate it with
    the value passed in "value". If no value is passed, initializes list
    with 101 values of 0.0.'''
    for i in range(101):
        new_value = copy.copy(value)
        lst.append(new_value)
    return lst   

my_list: list = []
my_list = init_list(my_list)



import gzip

def populate_list(file: str) -> tuple[list, int]:
    """This function uses init_list() to create an list of length 101, where each value is equal to 0.0. It loop through each line, and returns a list of the sums of all quality scores for each position."""
    my_list: list = []
    my_list = init_list(my_list)
    counter = 0 
    with gzip.open(file,"rt") as fh:
        for line in fh:
            counter += 1
            line = line.strip('\n')
            if counter%4 == 2:
                index = 0
                for base in line:
                    if base == "N":
                        my_list[index] += 1
                    index += 1 
          
    return my_list, counter  



my_list, num_lines = populate_list(file)


index = 0
for N_count in my_list:
    my_list[index] = N_count / (num_lines / 4) * 100
    index += 1


file_name = file.split("/")[6].split(".")[0]

import matplotlib.pyplot as plt

plt.plot(my_list, color = "red")
plt.title("N content per Base")
plt.xlabel("Base Position")
plt.ylabel("Percent N")
plt.savefig(f"N_Content_{file_name}.png")