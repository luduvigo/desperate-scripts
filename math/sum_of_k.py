###
# SUM OF THE FIRST K INTEGERS from 1 to T
# author: Paolo Antonio Rossi
###

import sys
 
T = int(sys.stdin.readline().rstrip())
 
for __ in range(T):
    n = int(sys.stdin.readline().rstrip())
    __ = sys.stdin.readline()
    print (n * (n - 1)) / 2
