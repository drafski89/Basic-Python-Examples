# This code will print out the entire folder list of the folder it's currently in
# It does not print the file names, just the folder names

import os

for root, dirs, files in os.walk('.'):
	for name in dirs:
		print (os.path.join(root,name))