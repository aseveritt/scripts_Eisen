#adapted from Sean Gibbons script

##TO locally install sklearn run "pip install --user scikit-learn " in your command line
##make sure input file isn't binary still "od kb_otu_table.biom |less > kb_otu_table.txt" and it doesn't have any weird rows " grep -v "*" kb_otu_table.txt > kb_otu_table1.txt

import numpy as np
from sklearn.decomposition import PCA
import pandas as pd

cwd= '/share/eisen/zshare2/aseveritt/PCA_sub'
inputfile= 'kb_otu_table1.txt'

#MAKE DF from BIOM table
col = ['sample']
for i in list(range(8)):
        col.append('OTU'+str(i)) #list of column names

table= pd.read_csv('{}/{}'.format(cwd,inputfile),delim_whitespace=True, header= None)
table.columns= col # name columns
table= table.set_index('sample')    # index by sample names
null_data = table[table.isnull().any(axis=1)]
print '**Warning: the following lines are missing data. All nulls will be filled with zeros'
print null_data
table= table.fillna(0)   #replace any missing values with zeros
table.to_csv(r'pd_df.csv')
print 'pandas dataframe saved as: pd_df.csv'
##REMOVING PC1
pca = PCA(n_components=8) #keeps 8 components? was 100 in original script-not sure why
#X = pca.fit_transform(table.apply(np.log(table))) #fit df into model 
X= pca.fit_transform(table)
#print X[1]
Y = X[:,1:] #Y = every value in list X except the first one
#print Y[1] 	#just showing that the first value is removed
untrans = pca.inverse_transform(X)  #get original data matrix back (w/out PC1 variance)
pca.components_ = pca.components_[1:] #remove the first PCA vector 
trans = pca.inverse_transform(Y)
print 'new pca vectors saved as: transformed_pca.txt'
with open('transformed_pca.txt' , 'w') as f:
	count =0
	while count < len(trans):
		f.write(trans[count])
		count += 1
