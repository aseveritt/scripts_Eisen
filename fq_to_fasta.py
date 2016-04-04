import os

fq=[]
cwd= '/home/aseveritt/ZosteraMarina/'
file_dir = '/home/aseveritt/ZosteraMarina'

for file in os.listdir('{}'.format(cwd)):
	#if file.endswith('494397.notZM.fq')== True:
	if file.endswith('.fq')== True:
		fasta=file[:-2]+'fasta' 
		with open (cwd+'/'+file,'r') as file1:
			lines=file1.readlines()
			os.chdir(file_dir)
			with open(fasta ,'w') as fastafile:
				count=0
				print "making:",fastafile
				while count < len(lines):
					fastafile.write('{}'.format(lines[count].replace("@",">")))
					fastafile.write('{}'.format(lines[count+1]))
					count +=4
