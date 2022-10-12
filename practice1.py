#!/usr/bin/env python3
# mlr 20221011

#practicing cooooooooool vim and python stuff

import sys

x= int(sys.argv[1]) 
print('The input is ' + sys.argv[1]) 

if x > 0: 
  if x % 2 == 0:
    print('Number is divisible by 2')
  elif x % 3 == 0:
    print('Number is divisible by 3')
  elif x % 4 == 0: 
    print('Number is divisible by 4') 
  elif x % 5 == 0: 
    print('Number is divisble by 5')
  elif x % 7 == 0:
    print('Number is divisible by 7')
  elif x % 11 == 0: 
    print('Number is divisible by 11')
  elif x % 13 == 0:
    print('Number is divisible by 13')
  elif x % 17 == 0:
    print('Number is divisible by 17')
  else: 
    print('Shes prime')

