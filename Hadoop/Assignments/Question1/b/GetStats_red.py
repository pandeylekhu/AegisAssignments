#!/usr/bin/env python
import sys,string
import numpy as np
comp_val_dict={}
for line in sys.stdin:
    line=line.strip()
    line=line.split(',')
    if line[0] in comp_val_dict:
        comp_val_dict[line[0]].append(float(line[1]))
    else:
	comp_val_dict[line[0]]=[float(line[1])]
for key in comp_val_dict.keys():
    larray=np.array(comp_val_dict[key])
    print('COMPANY NAME:'+key)
    print('MEAN:'+str(np.mean(larray)))
    print('MEDIAN:'+str(np.median(larray)))
    print('VARIANCE:'+str(np.var(larray)))
    print('STD:'+str(np.std(larray)))

