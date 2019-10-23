#!/usr/bin/env python
import sys,string
import numpy as np
import datetime
comp_val_dict={}
for line in sys.stdin:
    line=line.strip()
    line=line.split('\t')
    comp_val_dict[line[0]]=float(line[1])
sorted_keys=sorted(comp_val_dict.keys(),key=lambda x: datetime.datetime.strptime(x,'%d-%b-%Y'))
for idx in range(1,len(sorted_keys)):
    diff=float(comp_val_dict[sorted_keys[idx]])-float(comp_val_dict[sorted_keys[idx-1]])
    if diff>=-10 and diff<=10:
        print(sorted_keys[idx-1]+'\t'+str(comp_val_dict[sorted_keys[idx-1]])+'\t'+sorted_keys[idx]+'\t'+str(comp_val_dict[sorted_keys[idx]])+'\t'+str(diff))

