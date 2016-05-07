import subprocess, os
cwd = '/share/eisen/zshare2/aseveritt/ZosteraMarina/bowtie_outputs'

count = 0
for file in os.listdir(cwd):
	if file.endswith('_chloro')== True:
		sh= file[:10]+'.sh'
		shfile = open(sh, 'w')
        	shfile.write('#!/bin/bash \n')
		shfile.write('## \n')
		#shfile.write("#SBATCH -o /home/aseveritt/Phylosift/{}/out/{}.out \n".format(newfolder,file[:-6]))
                shfile.write("#SBATCH -e {}/{}.errors \n".format(cwd,file[:10]))
                #shfile.write("mkdir -p /home/aseveritt/Phylosift/{}/{} \n".format(newfolder,file[:-6]))
                #shfile.write("mkdir -p /home/aseveritt/Phylosift/{}/ps_log \n".format(newfolder))
               	#shfile.write("cd /home/aseveritt/Phylosift/{} \n".format(newfolder))
		shfile.write('python {}/remove_seq.py {} \n'.format(cwd,file))
		shfile.write("## \n")		
		shfile.close()
		
		path_to_sh = '{}/{}'.format(cwd,sh)	
       		print(subprocess.check_output('sbatch -N 1 -n 1 {}'.format(path_to_sh),shell=True)) #run the .sh file
      # 		break
