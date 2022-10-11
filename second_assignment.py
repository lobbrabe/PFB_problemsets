#!/usr/bin/env python3

import sys 

#my answer to problemset 2 of python unit

x = int(sys.argv[1])
print('The number being tested is ' + sys.argv[1])
if x > 0:
  print('Positive')
  if x < 50: 
    print('The number is less than 50')
  elif x > 50: 
    print('The number is greater than 50')
    if x % 3 == 0: 
      print('and divisible by 3')
elif x == 0: 
  print('The number is 0')
else:
  print('This is a negative number')

