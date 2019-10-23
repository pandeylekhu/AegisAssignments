#!/usr/bin/env python
import sys
import os
#company_name = os.environ['COMPANY_NAME'].upper()
#column=os.environ['COL'].upper()
company_name=sys.argv[1].upper()
column=sys.argv[2].upper()
col_pos=['SYMBOL','SERIES','OPEN','HIGH','LOW','CLOSE','LAST','PREVCLOSE','TOTTRDQTY','TOTTRDVAL','TIMESTAMP']
for line in sys.stdin:
    line = line.strip()
    if len(line)!=0:
        comp_name=line.split(',')[0]
        col_val=line.split(',')[col_pos.index(column)]
        if comp_name.upper() == company_name or (company_name == 'ALL' and comp_name <> 'SYMBOL'):
	    print(comp_name.upper()+','+col_val)

