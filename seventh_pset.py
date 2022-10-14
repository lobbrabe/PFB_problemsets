#!/usr/bin/env python3 
#mlr 20221013

#This is pset7: Regular Expressions 

import re
num_nob = []
with open ('Python_07_nobody.txt', 'r') as raw: 
	num_nob = len(re.findall(r"Nobody", raw.read()))
print(num_nob)


