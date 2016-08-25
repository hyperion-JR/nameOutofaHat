#!/usr/bin/python

import random
import sys

# Set league to the inputs and slice off the script name
league = sys.argv[1:]

# Function that takes in the list league and shuffles the list based on the number of iterations
def pickNameOutofHat(iterations):
	counter = 0
	while (counter <= iterations):
		counter += 1
		random.shuffle(league)
		print('Iteration '+str(counter)+' '+str(league))
	return league

print(pickNameOutofHat(100))
