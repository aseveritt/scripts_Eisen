cwd = '/home/aseveritt/Phylosift/Zostera/PS_temp/'

import os

for sample in os.listdir(cwd):                                          
	print 'working on:', sample,'\n'
	with open('{}{}/my_unique_test.nr_v119.wang.taxonomy'.format(cwd,sample), 'r') as infile:
		outfile = open('{}{}/my_unique_test.nr_v119.wang.taxonomy.nochloro'.format(cwd,sample), 'w')
		for line in infile.readlines():                             
			if "Chloroplast" not in line:
				outfile.write(line)
			else:
				continue  
