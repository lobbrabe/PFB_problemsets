#!/usr/bin/env python3
#mlr 20221012

#This is the fourth problemset: List and Loops 
import sys

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


#Part2: writing a while loop that prints 1-100

count = 1 

while count < 100:
  print(count)
  count +=1 
  if count == 100:
    print (count)
    break 
print('DOOOOOONE')


#Part3: while loop to calc the factorial of 100 

count = 10
total = []
final = 1 
while count >= 2: 
  final = count * final
  count -=1 
print(final)


#Part4: iterating through a loop using for loop, printing even values
Loops = [101,2,15,22,95,33,2,27,72,15,52] 
for loop in Loops: 
  if loop % 2 ==0:
    print(loop)

even_sum = 0
odd_sum = 0
sort_Loops = sorted(Loops, key=None, reverse=False) 
print(sort_Loops)
for loop in sort_Loops:
  print(loop)
  if loop % 2 ==0:
    even_sum = loop + even_sum  
  else: 
    odd_sum = loop + odd_sum 
print(f"'The even sum is' {even_sum}")
print(f"'The odd sum is' {odd_sum}") 


#Part5: Using range to print all numbers from 1-100
for num in range(101):
  print(num)

numbahs = [1 * x for x in range(101)]
print(numbahs)

first = int(sys.argv[1])
second = int(sys.argv[2]) + 1
for num1 in (range(first,second)):
  print(num1)


#Part6: for loop iterating through lists 
dna_list = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
dna_tup = []
for dna in dna_list: 
  print(f"{str(len(dna))} \t {dna}")
  length = str(len(dna)) 
  seqs = dna
  dna_tup = dna_tup.append(length + seqs)
print(dna_tup)

















 
