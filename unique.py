import os

cwd= '/home/aseveritt/Phylosift/Zostera/PS_temp/'


IDs=[]
for sample in os.listdir(cwd):                                              # for each sample
        print 'working on:', sample,'\n'
	with open('{}{}/my_test.fa'.format(cwd,sample), 'r') as infile:	    
		outfile = open('{}{}/my_unique_test.fa'.format(cwd,sample), 'w')
		f=infile.read().split('>')				    # split each seq apart
		count=0
		while count< len(f):		
			term= f[count].split('\n')			    #split the seq identifier
			identifier= term[0]
			if identifier not in IDs:			    #if not a repeat: 1) print 2) add to ID list
				#print ('>'+f[count])
				outfile.write('>'+f[count])
				IDs.append(identifier)
				count+=1
			elif identifier in IDs:				    #if a repeat: do nothing
				#print identifier, 'is a duplicate'
				count+=1
