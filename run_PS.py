import subprocess, os
cwd = '/home/aseveritt/Phylosift/'
PS_dir = '/share/eisen/zshare2/gjospin/Phylosift_test/phylosift'
concat_dir = '/share/eisen/zshare2/gjospin/misc/David/Berg1/phylosiftrc_concat'
newfolder = 'Zostera'

if not os.path.exists('{}{}'.format(cwd,newfolder)):
        os.mkdir('{}{}'.format(cwd,newfolder))
if not os.path.exists(cwd+'{}/sh_files'.format(newfolder)):
	os.mkdir(cwd+'{}/sh_files'.format(newfolder))
jobs= []
 
for file in os.listdir(cwd+newfolder):
	if file.endswith('.fasta')== True:
		sh= file[:-6] +'.sh'
               	logfile= file[:-6] + '.log'
		os.chdir('{}{}'.format(cwd,newfolder))

		shfile = open(sh, 'w')
        	shfile.write('#!/bin/bash \n')
		shfile.write('## \n')
		#shfile.write("#SBATCH -o /home/aseveritt/Phylosift/{}/out/{}.out \n".format(newfolder,file[:-6]))
                #shfile.write("#SBATCH -e /home/aseveritt/Phylosift/{}/err/{}.err \n".format(newfolder,file[:-6]))
                #shfile.write("mkdir -p /home/aseveritt/Phylosift/{}/{} \n".format(newfolder,file[:-6]))
                #shfile.write("mkdir -p /home/aseveritt/Phylosift/{}/ps_log \n".format(newfolder))
               	#shfile.write("cd /home/aseveritt/Phylosift/{} \n".format(newfolder))
		shfile.write('{} all --debug --config {} {} > {} 2>> {} \n'.format(PS_dir, concat_dir, file, logfile, logfile))
		shfile.write("## \n")		
		shfile.close()
		
		path_to_sh = '{}{}/{}'.format(cwd,newfolder,sh)	
       		print(subprocess.check_output('sbatch -N 1 -n 1 {}'.format(path_to_sh),shell=True)) #run the .sh file
               	#jobs.append(job_IDs[20:26])
       		break
	
#print 'Submitted',len(jobs),'batch jobs:\n'
#print jobs


