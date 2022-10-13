#!/usr/bin/env python3

#truth value statement 

import math

count=99
if count>70:
  count>70
  print('True, Number is greater than 70')
else:
  count<70
  print('Not True, Number is less than 70')

#checking if a number is positive or negative 
y=50
b=y/2
if y>0:
  print('Positive')
  if y< 50: 
    print('The number is less than 50')
    if (y/2) == (round(b,2)):
      print('It is an even number that is smaller than 50')
  elif y > 50:
    if y % 3 == 0:
      print('It is an even number, greater than 50, divisible by 3')
elif y==0:
  print('The number is 0')
else:
  print('Nagative')


#checking if a number is odd or even 
x=16 
a = x/2
if (x/2) != (round(a,2)): 
  print('The number is odd')
elif x == 0:
  print('The number is 0')
else: 
  print('The number is even')

