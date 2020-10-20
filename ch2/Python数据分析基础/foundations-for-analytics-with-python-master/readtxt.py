# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:06:44 2020

@author: CUMTYPJ
"""
#!/usr/bin/env python3
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
# 读取单个文本文件
input_file = sys.argv[1]
print ("Output #143: ")
filereader = open(input_file, 'r')
for row in filereader:
    print (row.strip())
filereader.close()