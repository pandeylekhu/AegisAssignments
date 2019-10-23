#!/usr/bin/env python
import sys
import os
company_name = os.environ['COMPANY_NAME']
mon_yyyy=os.environ['MON_YYYY']
#company_name=sys.argv[1].upper()
#mon_yyyy=sys.argv[2].upper()
 
for line in sys.stdin:
    line = line.strip()
    if len(line)!=0:
        numitem=len(line.split(','))
        if numitem<14:
            line=line+','*(14-numitem)
        word=line.split(',')[0]
        timestamp=line.split(',')[-4][3:]
        if word == company_name and mon_yyyy == timestamp:
	    #print(word,timestamp)
  	    print(1)

