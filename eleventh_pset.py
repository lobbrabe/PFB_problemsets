#!/usr/bin/env python3 
#mlr 20221016

#This is the eleventh python pset: classes 

class DNA_seq(object): 
	def __init__(self, sequence, name, organism): 
		self.sequence = sequence 
		self.name = name 
		self.organism = organism 
	
	#method to get seq length 
	def seq_length(self): 
		print(f"The length of {self.name} is {len(self.sequence)}")

	#method to get nucleotide comp	
	def nt_comp(self): 
		a_count = self.sequence.count('A') 
		t_count = self.sequence.count('T')
		g_count = self.sequence.count('G') 
		c_count = self.sequence.count('C') 
		total = len(self.sequence)
		print(f"A: {a_count/total} T: {t_count/total} G: {g_count/total} C: {c_count/total}") 

	#method that calculates GC content 
	def gc_content(self): 
		g_count = self.sequence.count('G') 
		c_count = self.sequence.count('C') 
		total = len(self.sequence)
		gc_cont = (g_count + c_count) / total
		print(f"The GC content is: {gc_cont}")

	#method to get out FASTA format 
	def fasta_form(self): 
		header = '>' + str(self.name) + ' ORG:' + str(self.organism) 
		main = self.sequence
		print(header, "\n",main) 

Samp1 = DNA_seq('ATCGGGGAATGACTTGAAAAAC', 'meike', 'homo')
Samp2 = DNA_seq('CTGGCGCGAAATAGGTGATC', 'jules', 'homo') 

for d in [Samp1, Samp2]: 
	print('name: ', d.name, ' ', 'seq: ', d.sequence) 
	print('name: ', d.name, ' ', 'organism: ', d.organism) 
	d.seq_length() 
	d.gc_content() 
	d.nt_comp()
	d.fasta_form()

	
