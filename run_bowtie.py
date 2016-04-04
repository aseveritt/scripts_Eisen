
import os, subprocess
cwd= '/home/aseveritt/ZosteraMarina'
file_dir= '/home/aseveritt/ZosteraMarina/Zostera'
index = 'chloro_ref'

##to make reference##
# bowtie2-build chloro_ref o.sativa_chloroplast.fa

for sample in os.listdir(file_dir):
        os.chdir('{}'.format(cwd))
        shfile= open('run_{}.sh'.format(sample),'w')
        shfile.write('#!/bin/bash \n')
        shfile.write('## \n')
	shfile.write('#module load bowtie2')
        shfile.write('#bowtie2 --local -x {} -f -U {}/{} > {}_chloro'.format(index,file_dir,sample,sample))
        shfile.close()

        path_sh= '{}/run_{}.sh'.format(cwd,sample)
        print (subprocess.check_output('sbatch -N 1 -n 1 {}'.format(path_sh),shell=True)) #run the .sh file


