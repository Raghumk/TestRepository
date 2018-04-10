
#Iterator and Generator
#iterator allows programmer to travers through elements

import sys
import math
list=[1,2,3,4]

it = iter(list)   # this builds the iterator.   "iter" keyword is used.

'''
while True:
	try:
		print(next(it))
	except StopIteration:
		Sys.exit()

'''