##########################################################################
# Simple python script that is adding braces in if conditions of C++ files
#
# author: luduvigo
##########################################################################


import sys

infile, outfile = sys.argv[1], sys.argv[2]

# Read file
inf = open(infile)
conta = 0
# Write file.
out = open(outfile,"w")
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
