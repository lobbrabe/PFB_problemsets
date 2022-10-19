#!/usr/bin/env python3 
#mlr 20221018

sequence = 'GCCACAGAGCCTAGGACCCCAACCTAACCTAACCTAACCTAACCTACAGTTTGATCTTAACCATGAGGCTGAGAAGCGATGTCCTGACCGGCCTGTCCTAACCGCCCTGAC'
kmer_length = 6 

def sequence_to_kmer_list(sequence, kmer_length): 
    kmer_list = list ()

    for nt in range(len(sequence)): 
        kmer = sequence [nt:nt+kmer_length]
        kmer_list.append(kmer)
        for kmer in kmer_list: 
            if len(kmer) < kmer_length: 
                kmer_list.remove(kmer)
                print(kmer_list) 



run1 = sequence_to_kmer_list(sequence, kmer_length) 
print(run1)
 
