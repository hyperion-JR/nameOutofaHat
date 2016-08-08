
import random

# Enter names into the list called league.
league = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6']

# Function that takes in the list league and shuffles the list based on the number of iterations
def draftOrder(iterations):
	counter = 0
	while (counter <= iterations):
		counter += 1
		random.shuffle(league)
		print('Iteration '+str(counter)+' '+str(league))
	return league

print(draftOrder(100))