#!/usr/bin/env python3
#mlr 20221012

#This is the fourth problemset: List and Loops 

taxa = 'sapiens, erectus, neanderthalensis'
print(taxa)
print(taxa[1])
print(type(taxa))

species = taxa.split(', ')
print(species)
print(species[1])
print(type(species))

sort_species = sorted(species, key=str.lower, reverse=False)
print(sort_species)

sortlen_species = sorted(species, key=len, reverse=False)
print(sortlen_species)


