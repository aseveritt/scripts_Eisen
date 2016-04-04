cwd='/share/eisen/zshare2/gjospin/Slims_Eisenlab_backup/berg1_Miseq300_20160208/demul_redo/raw_fastq' #path to files
a5_dir= '/home/gjospin/software/a5_miseq_linux_20140502/bin/'
newfolder='berg' 

import os,subprocess

mate1 =[]
mate2 =[]
for file in os.listdir('{}'.format(cwd)):
	if file.endswith('1.fastq.gz')== True:
		mate1.append(file)	
	elif file.endswith('2.fastq.gz')==True:
		mate2.append(file)
	else:
		continue

if not os.path.exists('/home/aseveritt/assemblies/{}'.format(newfolder)):
	os.mkdir('/home/aseveritt/assemblies/{}'.format(newfolder))
if not os.path.exists('/home/aseveritt/assemblies/{}/sh_files'.format(newfolder)):
	os.mkdir('/home/aseveritt/assemblies/{}/sh_files'.format(newfolder))
if not os.path.exists('/home/aseveritt/assemblies/{}/out'.format(newfolder)):
	os.mkdir('/home/aseveritt/assemblies/{}/out'.format(newfolder))
if not os.path.exists('/home/aseveritt/assemblies/{}/err'.format(newfolder)):
	os.mkdir('/home/aseveritt/assemblies/{}/err'.format(newfolder))
jobs=[]
count=0
while count<len(mate1): 
#while count==0:
	for i in mate1:
		for j in mate2:
			if i[:-10]==j[:-10]:    ## if ID matches
				filename=i[:-11]
				filename2= filename +'.sh'
				os.chdir('/home/aseveritt/assemblies/{}/sh_files'.format(newfolder))

				file = open (filename2,'w')		##make file named mate prefex i 
				file.write("#!/bin/bash \n")
				file.write("## \n")
				file.write("#SBATCH -o /home/aseveritt/assemblies/{}/out/{}.out \n".format(newfolder,filename))
				file.write("#SBATCH -e /home/aseveritt/assemblies/{}/err/{}.err \n".format(newfolder,filename))
				file.write("mkdir -p /home/aseveritt/assemblies/{}/{} \n".format(newfolder,filename))
				file.write("mkdir -p /home/aseveritt/assemblies/{}/ps_log \n".format(newfolder))
				file.write("cd /home/aseveritt/assemblies/{}/{}  \n".format(newfolder,filename))
				file.write("{}/a5_pipeline.pl --threads=12 {}/{} {}/{} {} > {}.log 2>> {}.log \n".format(a5_dir,cwd,i,cwd,j,filename,filename,filename))
				file.write("cd /home/aseveritt/assemblies/{} \n".format(newfolder))
				file.write("## \n")
				file.close() 
				
				path_sh= '/home/aseveritt/assemblies/{}/sh_files/{}'.format(newfolder,filename2)
				job_IDs= subprocess.check_output('sbatch -N 1 -n 1 {}'.format(path_sh),shell=True) #run the .sh file
				jobs.append(job_IDs[20:26])
				count +=1
				break

print 'Submitted',len(jobs),'batch jobs:\n'
print jobs
