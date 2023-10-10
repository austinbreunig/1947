import pandas as pd
import numpy as np
mc=pd.read_csv('mc_practice1.csv',index_col=0)
all_loc=pd.read_csv('all_loc_practice.csv')

mc_int=mc.loc[:,['INT loc','INT lat','INT long']]
#print(mc_int)
#print(all_loc)

#Locations that need to be added to All Locations List
filter0=mc_int.iloc[:,0].isin(all_loc.iloc[:,0])
false_int=filter0.index[filter0==False].tolist()
#print(false_int)

#Filter INT locations and return indexes that are TRUE
filter1=mc_int.iloc[:,0].isin(all_loc.iloc[:,0])
true_int=filter1.index[filter1== True].tolist()
#print('locations that are in', true_int)

#Filter INT latitudes and return indexes that are FALSE
filter2=mc_int.iloc[:,1].isin(all_loc.iloc[:,1])
false_lat=filter2.index[filter2==False].tolist()

#filter INT longitudes and return indexes that are FALSE
filter3=mc_int.iloc[:,2].isin(all_loc.iloc[:,2])
false_long=filter3.index[filter3== False].tolist()

corrections=[]
for i in true_int:
    for x in false_lat:
        if i==x:
            corrections.append(i)
for i in true_int:
    for y in false_long:
        if i==y:
            corrections.append(i)

final=list(set(corrections))
#print('Locations with incorrect coordinates',final)
