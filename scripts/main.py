import re



file = open("data/orf_coding_all.fa.txt", "r")

genes ={} # dictionary to hold: key - gene name, value - sequence
name = ""
seq = ""
for line in file:
    line = line.strip("\n")
    if line[0] == ">":
        if seq != "" and name != "":
            genes[name] = seq
        name = line
        seq = "" 
    elif line != "\n" or None:
        seq += line
        
if seq != "" and name != "": # to add the last gene in the file
    genes[name] = seq

file.close()