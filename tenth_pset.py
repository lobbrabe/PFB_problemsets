#!/usr/bin/env python3 
#mlr 20221014

#This is problemset 10 for Programming for Biology: Functions
#DIRECTIONS: This file must receive two inputs, one fasta or text file and a number that represents how many nts you want in each line. 

import sys 

#this function takes fasta files and reformats them to have lines with a given nt length
def print_dna_nt_lines(dna, length):
	format_dna = ''
	length = int(length)
	dna = dna.replace('\n', '')
	for nt in range(len(dna)):
		format_dna += dna[nt] 
		if (nt+1) %length==0:
			format_dna += '\n'
	return format_dna  

#this function calculates the GC content of a given dna sequence 
def gc_count(dna): 
	g_count = dna.count('G') 
	c_count = dna.count('C') 
	length = len(dna) 
	total = (g_count + c_count) / length
	return total 

#this function gives the reverse compliment of a given dna sequence 
def reverse_comp(seq): 
	seq1 = seq.lower()
	seq2 = seq1.replace('t','A')
	seq3 = seq2.replace('a','T') 
	seq4 = seq3.replace('c','G')
	seq5 = seq4.replace('g','C') 
	final_rev_comp = seq5[::-1] 
	return final_rev_comp 


input_file = sys.argv[1]
length = sys.argv[2]

genes = {}
with open (input_file, 'r') as raw: 
        for line in raw:
                line = line.rstrip()
                if line.startswith('>'):
                        header = line 
                        genes[header]=''
                else: 
                        genes[header] += line

for gene,seq in genes.items():
	reformat = print_dna_nt_lines(seq, length)
	print(f"{gene}\n{reformat}") 
print('All Done :)') 
 

dna = 'CGTGCTTTCCACGACGGTGACACGCTTCCCTGGA'
GCcontent = gc_count(dna) 
print(GCcontent)

revcomp = reverse_comp(dna)
print(revcomp) 

 


