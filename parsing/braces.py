##########################################################################
# Simple python script that is adding braces in if conditions of C++ files.
# This script has the goal to help me automatize a little bit the 
# insertion of braces after around 18000 if that have one line statements 
# after them.
#
# param: input source file that we want to modify
#
# author: luduvigo (paoloantoniorossi@gmail.com)
##########################################################################


import sys
import shutil
import string

infile = sys.argv[1]

# Backup of the file modified
shutil.copyfile(infile, infile + '.backup')
# Read file
inf = open(infile + '.backup')
# Write file.
out = open(infile,"w")
skip = False
space = ""
for line in inf.readlines():
	if "//" in line or "/*" in line:
		out.write(line)
		print "Skipped comment!"
		skip = False
	elif skip == True:
		if line == '\n':
			print "found an end of line"
			out.write(line)
		elif "{" in line or "&&" in line or "||" in line or "if" in line:	
			out.write(line)
			print "-> brace already there"
			skip = False
		else:
			dist = len(line) - len(line.lstrip())
			out.write( space + '{\n' )
			out.write( space + '\t' + line.lstrip() )
			out.write( space + '}\n')
			print "-> braces added"
			skip = False
	elif "if(" in line and line[-2] == ')':
		out.write(line)
		dist = len(line) - len(line.lstrip())
		space = line[:dist]
		print "Found: " + line[:-1]
		skip = True
	elif "if (" in line and line[-2] == ")" :
		out.write(line)
		dist = len(line) - len(line.lstrip())
		space = line[:dist]
		print "Found: " + line[:-1]
		skip = True
	else:
		out.write(line)
out.close()
