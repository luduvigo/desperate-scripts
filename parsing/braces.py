##########################################################################
# Simple python script that is adding braces in if conditions of C++ files
#
# author: luduvigo
##########################################################################


import sys
import shutil

infile = sys.argv[1]


# Backup of the file modified
shutil.copyfile(infile, infile + '.backup')
# Read file
inf = open(infile + '.backup')
# Write file.
out = open(infile,"w")
skip = False
for line in inf.readlines():
	if skip == True:
		if "{" in line: 
			out.write(line)
			print "-> brace already there"
		else:
			out.write('{\n')
			out.write('\t' + line)
			out.write('}\n')
			print "-> braces added"
		skip = False
	elif "if(" in line and line[-2] == ')':
		out.write(line)
		print "Found: " + line[:-1]
		skip = True
	elif "if (" in line and line[-2] == ")" :
		out.write(line)
		print "Found: " + line[:-1]
		skip = True
	else:
		out.write(line)
out.close()
