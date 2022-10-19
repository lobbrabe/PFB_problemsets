#!/usr/bin/env python3 
#mlr 20221018

kmer_list = ['ACTGCA', 'CTGCAT', 'TGCATC', 'GCATCC', 'CATCCT', 'ATCCTG', 'TCCTGG', 'CCTGGA', 'CTGGAA', 'TGGAAA', 'GGAAAG', 'GAAAGA', 'AAAGAA', 'AAGAAT', 'AGAATC', 'GAATCA', 'AATCAA', 'ATCAAT', 'TCAATG', 'CAATGG', 'AATGGT', 'ATGGTG', 'TGGTGG', 'GGTGGC', 'GTGGCC', 'TGGCCG', 'GGCCGG', 'GCCGGA', 'CCGGAA', 'CGGAAA', 'GGAAAG', 'GAAAGT', 'AAAGTG', 'AAGTGT', 'AGTGTT', 'GTGTTT', 'TGTTTT', 'GTTTTT', 'TTTTTC', 'TTTTCA', 'TTTCAA', 'TTCAAA', 'TCAAAT', 'CAAATA', 'AAATAC', 'AATACA', 'ATACAA', 'TACAAG', 'ACAAGA', 'CAAGAG', 'AAGAGT', 'AGAGTG', 'GAGTGA', 'AGTGAC', 'GTGACA', 'TGACAA', 'GACAAT', 'ACAATG', 'CAATGT', 'AATGTG', 'ATGTGC', 'TGTGCC', 'GTGCCC', 'TGCCCT', 'GCCCTG', 'CCCTGT', 'CCTGTT', 'CTGTTG', 'TGTTGT', 'GTTGTT', 'TTGTTT', 'TTGTTT', 'TTGTTT']

kmer_count_dict = dict()
for kmer in kmer_list: 
    if kmer in kmer_count_dict:   
        kmer_count_dict[kmer] += 1 
    else: 
        kmer_count_dict[kmer] = 1 
print(kmer_count_dict) 
