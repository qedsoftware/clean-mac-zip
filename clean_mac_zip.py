#!/usr/bin/env python
import os, sys
if len(sys.argv) < 2:
	print "Please provide the name of the .zip you wish to clean."
	sys.exit()
	
zip_file = sys.argv[1]
os.system("zip -d %s *DS_Store*" % zip_file)
os.system("zip -d %s *__MACOSX*" % zip_file)
print "Cleaned zip contents:"
os.system("unzip -l %s" % zip_file)