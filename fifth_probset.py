#!/usr/bin/env python3 
#mlr 20221013

#This is the Python5 problemset 
import sys


#Part1: creating a dictionary of some of my fav things 

fav_dict = {
		'book': '1984',
		'story': 'The husband stitch',
		'food': 'Doner', 
		'tree': 'sequoia' }
print(fav_dict)
print(fav_dict['book'])

fav_thing = 'book' 
print(fav_dict[fav_thing]) 

fav_tree = 'tree'
print(fav_dict[fav_tree]) 

fav_dict['organism'] = 'raccoon'
print(fav_dict) 

fav_thing = 'organism' 
print(fav_dict[fav_thing]) 


#Part2: input from command line 
tippy = input("What would you like to know my favorite of? ") 
print(fav_dict[tippy])

#Part3: change favorite organsim from command input 
changed = input("waht organism is your favorite? ")
fav_dict['organism'] = changed
print(f"My new fav organism is now: {fav_dict['organism']}") 


