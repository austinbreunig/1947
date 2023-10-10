import pandas as pd
import numpy as np
mc=pd.read_csv('Master_checklist.csv',index_col=0)
all_loc=pd.read_csv('all_locations.csv')

#identify Interview columns
mc_int=mc[mc.columns[:3]]

#Locations that need to be added to All Locations List
filter0=mc_int.iloc[:,0].isin(all_loc.iloc[:,0])
addto_allLoc_int=filter0.index[filter0==False].tolist()
print(addto_allLoc_int)

#Filter Interview locations and return indexes that are TRUE
filter1=mc_int.iloc[:,0].isin(all_loc.iloc[:,0])
true_int=filter1.index[filter1== True].tolist()

#Filter INT latitudes and return indexes that are FALSE
filterIntLat=mc_int.iloc[:,1].isin(all_loc.iloc[:,1])
false_lat=filterIntLat.index[filterIntLat==False].tolist()

#filter INT longitudes and return indexes that are FALSE
filter3=mc_int.iloc[:,2].isin(all_loc.iloc[:,2])
false_long=filte
r3.index[filter3== False].tolist()

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
print('Locations with incorrect coordinates',final)
