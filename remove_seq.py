#script must be run with wrapper.py
import os,sys

cwd= '/share/eisen/zshare2/aseveritt/ZosteraMarina/bowtie_outputs'   #path to bowtie output
fasta_dir= '/home/aseveritt/ZosteraMarina/Zostera' 		     #path to original fasta output
str_len =10							     #length of sample names	
newfolder= 'Left_afterbowtie'					     #newfoldername

if not os.path.exists('{}/{}'.format(cwd,newfolder)):
	os.mkdir('{}/{}'.format(cwd,newfolder))


bowtielist=[]
sample= sys.argv[1]
with open (sample,'r') as b:					#open bowtie file
	for line in b:
		#if 'SRR1692420.111631813' in line:
		#	break
		if line.split()[0].startswith('S') and line.split()[1] != "4":		#if seq aligned aligned
			bowtielist.append('>'+(line.split())[0])			#add IDs into a list in fasta format
#print len(bowtielist)		
for fasta in os.listdir(fasta_dir):
	if fasta.startswith(sample[:10]) and fasta.endswith('.fasta'):		#for the corresponding fasta file
	#if fasta.startswith('test') and fasta.endswith('.fasta'):	
                with open('{}/{}'.format(fasta_dir,fasta),'r') as f:			# open fasta file
			print 'fastafile:', fasta
			#with open('{}/{}/tester'.format(cwd,newfolder),'w') as newfile:
			with open('{}/{}/{}'.format(cwd,newfolder,sample[:10]),'w') as newfile:		#open newfile
				for line in f:
					if line.startswith('>') and (line.split()[0] not in bowtielist):	#if seq did not map in bowtie
						newfile.write(line)						#print fasta format 
						newfile.write(f.next())
