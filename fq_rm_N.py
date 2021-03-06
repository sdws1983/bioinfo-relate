#!/usr/bin/env python

import sys, getopt
import re
import time

def get_option():
	opts, args = getopt.getopt(sys.argv[1:], "hi:o:")
	input_file = ""
	output_file = ""
	h = ""
	for op, value in opts:
		if op == "-i":
			input_file = value
		elif op == "-o":
			output_file = value
		elif op == "-h":
			h = 'useages:\nremove the sequence which contain "N"\n-i : inputfile\n-o : outputfile\n'
	return input_file,output_file,h

def main(input_file, output_file):
	fout = open(output_file, 'w')
	all = []
	count = 1
	with open (input_file) as f:
		for i in f:
			#print (i)
			if ((int(count)) % 4) == 0:
				all.append(i)
				if re.findall("N",all[1]):
					all = []
				else:
					fout.write(''.join(all))
					all = []
			else:
				all.append(i)
			count += 1
	fout.close()

if __name__ == "__main__":
	time_start = time.time()

	input_file,output_file,h = get_option()
	if str(h) == "":
		main(input_file, output_file)
		print ("time: " + str (time.time()-time_start))
	else:
		print (h)
