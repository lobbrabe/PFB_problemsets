#!/usr/bin/env python3
#mlr 20221014

#This is the eight problemset for PfB: Data Structures 

#Part1: calc nt comp from a file 

import re

#Opening file and separating it into a gene:seq dict
genes = {}
final_header = ''
with open ('Python_08.fasta.txt', 'r') as raw: 
    for line in raw:
        line = line.rstrip()
        if line.startswith('>'):
            header = line
            new_header = header.split()
            final_header = str(new_header[0])
            genes[final_header]=''
        else: 
            genes[final_header] += line
#print(genes)

#Getting ATCG counts for all genes
for gene,seq  in genes.items(): 
    A_count = seq.count('A') 
    T_count = seq.count('T') 
    C_count = seq.count('C') 
    G_count = seq.count('G') 
#    print(f"{gene} A: {A_count} T: {T_count} C: {C_count} G: {G_count}")

#Getting codons for all genes, into a separate dict 
codon_genes = ''
codons = {}
for gene,seq in genes.items():
    codon_genes = re.findall(r"[ATCG]{3}", seq)
    codons[gene] = codon_genes
#print(codons)
            

#Reverse complimenting each sequence and get

