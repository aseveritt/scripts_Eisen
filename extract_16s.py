import os
from subprocess import check_output
cwd = '/home/aseveritt/Phylosift/Zostera/PS_temp/'

## extract 16s data###
for sample in os.listdir(cwd):                                              # for each sample
	print 'working on:', sample,'\n'
	newfile=open('{}{}/my_test.fa'.format(cwd,sample),'a')
	os.chdir('{}{}/alignDir'.format(cwd,sample))
	for data_set in os.listdir('{}{}/alignDir'.format(cwd,sample)):     #for all seq files that mapped in alignDir
		if str(data_set).startswith('16s'):
			if str(data_set).endswith('.tmp')==False:           #if not a repeat
				print "adding:", data_set
				oldfile = open(data_set,'r')
				while True:
					char=oldfile.read(1)
					line= oldfile.readline(1)
					print line
					if not char:                        # if at end of file
						break
					elif char=='-' or char== '.':       #remove filler info
						continue
					else:							
						newfile.write(char)
		else:					
			continue



	
	##run mothur##
#	os.chdir('{}{}'.format(cwd,sample))
#	shfile= open('run_my_test.sh','w')
#	shfile.write('#!/bin/bash \n')            
#        shfile.write('## \n')
#        shfile.write('/home/dwu/bin/mothur/mothur "#classify.seqs(fasta=my_test.fa, template=/share/eisen/zshare3/dwu/DB/SILVA/for_muthor/silva.nr_v119.align, taxonomy=/share/eisen/zshare3/dwu/DB/SILVA/for_muthor/silva.nr_v119.tax, method=wang)"')
#        shfile.close()

#        path_sh= '{}{}/run_my_test.sh'.format(cwd,sample)
#        print check_output('sbatch -N 1 -n 1 {}'.format(path_sh),shell=True) #run the .sh file

