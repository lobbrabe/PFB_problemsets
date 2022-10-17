#!/usr/bin/env python3
#mlr 20221016

#This is the biopython pset

from Bio import SeqIO 
from Bio.SeqUtils import GC 

seq_count = 0

length = 0
max_length = 0 
min_length = 10000000000000000000000000

gc_quant = 0 
max_gc = 0 
min_gc = 100

for seq_record in SeqIO.parse("Python_08.fasta", "fasta"): 
	seq_count = seq_count + 1
	print('ID', seq_record.id) 
	print('Sequence', seq_record.seq)
	print('Length', len(seq_record.seq))
	length = length + len(seq_record.seq)

	#find longest and shortest seq
	if len(seq_record.seq) > max_length: 
		max_length = len(seq_record.seq) 

	if len(seq_record.seq) < min_length: 
		min_length = len(seq_record.seq)

	#calculate GC content 
	g_count = seq_record.seq.count('G') 
	c_count = seq_record.seq.count('C') 
	total_count = seq_record.seq.count('')
	gc_content = (g_count + c_count)/total_count
	gc_quant = gc_quant + gc_content 
	print(f"GC content: {gc_content}") 

	#calculate GC max min avg
	if gc_content > max_gc: 
		max_gc = gc_content 
	if gc_content < min_gc: 
		min_gc = gc_content 

print('\n','Summary of all genes') 
print(f"Sequence count: {seq_count}")
print(f"Total number of nts: {length}")	
print(f"Max length: {max_length}")	
print(f"Min length: {min_length}")
print(f"Average length: {length/seq_count} nt/gene")
print(f"Max GC content: {max_gc}") 
print(f"Min GC content: {min_gc}") 
print(f"Average GC content: {gc_quant/seq_count} gc/gene")

 




