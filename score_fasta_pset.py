#!/usr/bin/env python3 
#mlr 202210121

#This is the fasta excercise examining best paramaters for different comparisons 

import sys, re
import pandas as pd  

#reading and parsing the file 

ssearch_file = sys.argv[1:] 

parsed_dfs = []

for ss_file in ssearch_file: 
    ss_df = pd.read_csv(ss_file, sep= '\t', comment='#', header=None)
    parsed_df = ss_df.iloc[:,[2, 3, 10]]
    if parsed_df not in parsed_dfs: 
        parsed_dfs.append(parsed_df) 
e

final_df = pd.concat(parsed_dfs) 
print(final_df)  

#get columns from table corresponding to precid, alen, evalue 
#parsed_df = ss_df.iloc[:,[2, 3, 10]]
#frames = []
#final_df = pd.concat(frames) 

#add columns to new table 


