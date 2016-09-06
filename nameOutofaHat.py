#!/usr/bin/python

import random
import sys

# Set league to the inputs and slice off the script name
league = sys.argv[1:]
verbose = '-v' in league
if verbose:
	league.remove('-v')

# Function that takes in the list league and shuffles the list based on the number of iterations
def pickNameOutofHat(iterations):
	for counter in range(iterations):
		random.shuffle(league)
		if verbose:
			print('Iteration {} {}'.format(counter + 1, league))
	return league

print(pickNameOutofHat(100))
