#test that index of reduced dataset is index of actual dataset

#import libraries
import numpy as np
import pandas as pd
import scipy.constants as sci

#%% - read in datasets


#reduced dataset
red_data=pd.read_csv('/homes/masmith/thesis/reduced_dataset.csv')
#drop the extra column
red_data=red_data.drop(columns=['Unnamed: 0'])
#disregard ind column, not actually the index
print('reduced dataset collected')

#full dataset
full_data=pd.read_csv('/homes/masmith/thesis/big_data_freqs.csv')
#drop the extra column
full_data=full_data.drop(columns=['Unnamed: 0'])
#make new list for emitted frequency
fem=[]
for val in full_data['fobs']:
    fem.append(2*val)
#make new column for strain amps
hs=[]
for i in range(full_data['m_host'].size):
    # hs.append((4*(np.pi**(2/3))*(sci.G*mergeddf['chirpmass(kg)'][i])**(5/3))/ \
    #           ((sci.c**4)*((1/(2*mergeddf['fobs'][i]))**(2/3))*mergeddf['lum_dist(m)'][i]))
    hs.append((4*((sci.G*full_data['chirpmass(kg)'][i])**(5/3))*(np.pi*(fem[i]))**(2/3))/ \
              ((sci.c**4)*full_data['lum_dist(m)'][i]))
full_data.insert(1,'h',hs)
print('full dataset collected')


#%% - finding indicies


#make list of reduced strains
strains_red=list(red_data['s'])

#make list of reduced strains and indicies
strains_full=list(full_data['h'])
index_full=list(full_data.index.values)
sort_full=list(zip(index_full,strains_full))

#I want to know the indicies in full of the bhbs in red
pick_in=[]
for val in strains_red:
    for num in strains_full:
        if val==num:
            pick_in.append(strains_full.index(num))
print(pick_in)
