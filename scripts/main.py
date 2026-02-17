import re



file = open("data/orf_trans_all.fa.txt", "r")

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

zinc_finger_found_counter = 0
protein_and_zinc_finger_sequence = {} # dictionary to hold: key - gene name, value - sequence of the zinc finger motiv

motif_pattern = r"(?=(C.H.[LIVMFY]C..C[LIVMYA]))"

for gene_name, sequence in genes.items():
    matches = re.findall(motif_pattern, sequence)
    
    if matches:
        zinc_finger_found_counter += 1
        protein_and_zinc_finger_sequence[gene_name] = matches

# Write results to output file
with open("results/yeast_zinc_finger_orf.txt", "w") as output_file:
    for gene_name, motifs in protein_and_zinc_finger_sequence.items():
        output_file.write(f"{gene_name}\n")
        for m in motifs:
            output_file.write(f"{m}\n")
        output_file.write("\n")
    
    output_file.write(f"Total proteins containing Zinc Finger Motif: {zinc_finger_found_counter}\n")

print("Finished")