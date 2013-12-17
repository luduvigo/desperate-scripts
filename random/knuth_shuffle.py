###################################################
# Simple python script that shuffles the element of 
# an input file using the Knuth algorithm
#
# param: input source file that we want to shuffle
#
# author: luduvigo (paoloantoniorossi@gmail.com)
###################################################

import sys
import random


def knuth_shuffle(data):
	N = len(data)
	for i in range(N - 1):
		swap(data, i, random.randrange(i, N))
	return data

def swap(data, i, j):
	print "swap", i, j
	data[i], data[j] = data[j], data[i]

###############################################
# Calling the shuffle function
#
# Read the elements from a file
# splitting them inside a list
infile = sys.argv[1]
in_file = open(infile,"r")
text = in_file.read()
in_file.close()

# Apply the Knuth simple shuffle algorithm
res = knuth_shuffle(text.split())

#Check if we are 
error = False
for a in text.split():
	if a not in res:
		error = True
if not len(res) == len(text.split()):
	error = True

if error:
	print "Ops! Something went wrong"
else:
	print "Done!"


# Save the results in a .shuffled file
out = open(infile + ".shuffled","w")
for i in res:
	out.write(i + " ")
out.close

