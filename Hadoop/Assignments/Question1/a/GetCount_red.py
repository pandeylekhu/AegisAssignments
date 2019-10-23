#!/usr/bin/env python
import sys,string
count=0
for line in sys.stdin:
    line=line.strip()
    count=count+int(line)
print(count)
