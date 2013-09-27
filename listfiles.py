#!/usr/bin/python

from os import listdir

def recursiveList( path, more_levels= -1, prefix= "" ):
	try: 
		for fname in listdir( path ):
			listed= path + '/' + fname
			listed= listed.replace( '//', '/' )
			print prefix + listed
			if more_levels != 0:
				recursiveList( listed, more_levels - 1, prefix + "    " )
	except OSError:
		print prefix + "Permission denied."
	except:
		print prefix + "Something else happened."
	finally:
		pass

recursiveList( "/" )
