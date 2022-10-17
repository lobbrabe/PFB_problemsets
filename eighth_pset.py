#!/usr/bin/env python3
#mlr 20221014

#This is the eight problemset for PfB: Data Structures 

#Part1: calc nt comp from a file 

genes = {}
with open ('Python_08.fasta.txt', 'r') as raw: 
	for line in raw:
		line = line.rstrip()
		if line.startswith('>'):
			header = line 
			genes[header]=''
		else: 
			genes[header] += line
print(genes)		




#gene_id, length, path, seq = line.split()
#		for gene_id in raw: 
#			for length in genes[gene_id]: 
#				for path in genes[gene_id][length]: 
#					for seq in genes[gene_id][length][path]: 
#						genes = genes.append()

