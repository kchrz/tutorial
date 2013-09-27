#!/usr/bin/python

from os import listdir

for fname in listdir( "/" ):
	print "/" + fname
	
	try:
		for subname in listdir( "/" + fname ):
			print "    /" + fname + "/" + subname
	except OSError:
		print "   Permission denied"
		pass
		
	
