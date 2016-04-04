import os, subprocess
cwd= '/home/aseveritt/Phylosift/Zostera/PS_temp/'

for sample in os.listdir(cwd):
	os.chdir('{}{}'.format(cwd,sample))
	shfile= open('run_my_test.sh','w')
	shfile.write('#!/bin/bash \n')
	shfile.write('## \n')
	shfile.write('/home/dwu/bin/mothur/mothur "#classify.seqs(fasta=my_unique_test.fa, template=/share/eisen/zshare3/dwu/DB/SILVA/for_muthor/silva.nr_v119.align, taxonomy=/share/eisen/zshare3/dwu/DB/SILVA/for_muthor/silva.nr_v119.tax, method=wang)"')
	shfile.close()
			
	path_sh= '{}{}/run_my_test.sh'.format(cwd,sample)
	print (subprocess.check_output('sbatch -N 1 -n 1 {}'.format(path_sh),shell=True)) #run the .sh file


