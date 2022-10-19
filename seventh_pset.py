#!/usr/bin/env python3 
#mlr 20221013

#This is pset7: Regular Expressions 

import re
num_nob = []
with open ('Python_07_nobody.txt', 'r') as raw: 
	num_nob = len(re.findall(r"Nobody", raw.read()))
print(num_nob)


#replacing word in exisiting file and writing new file
with open ('Python_07_nobody.txt', 'r') as raw, open('Julianna.txt', 'w') as output:
	for line in raw: 
		line = line.rstrip()	
		replace_raw = re.sub(r"Nobody", r"Julianna", raw.read())  
#		print(replace_raw) 


#fasta header parser 
header = {}
seq = ''
with open ('Python_07.fasta', 'r') as raw: 
	for line in raw: 
		line = line.rstrip()
		if line.startswith('>'): 
			header_split = line.split(" ", 1)  
			header[header_split[0]] = header_split [1]
		else: 
			seq += line
for gene_id, desc in header.items(): 
	header[gene_id] = desc
#	print(f"ID: {gene_id}, DESC: {desc}\n{seq}")


#find ApoI restriction enzyme site in fasta file
header1 = ''
seq1 = ''
replace_seq1 = ''
apoi_site = re.findall(r"[AG]AATT[CT]", seq1) 
with open ('Python_07_ApoI.fasta.txt', 'r') as raw: 
	for line in raw: 
		line = line.rstrip()
		if line.startswith('>'): 
			line = header1	
		else: 
			seq1 += line 
		replace_seq1 = re.sub(r"[AG]AATT[CT]", r"^", seq1) 

print(f"Cut sites for ApoI: {replace_seq1}")  

frag_len_dict = []		
sorted_frags = [] 
split_apoi = replace_seq1.split("^") 
sorted_frags = sorted(split_apoi, key=len) 
print(sorted_frags)


#for seqs,lengths in frag_len_dict: 
#	sorted_frags = sorted(lengths) 
# 	print(sorted_frags) 


#sort_split_apoi = sorted(str(len(split_apoi))) 
#print(sort_split_apoi)

 



