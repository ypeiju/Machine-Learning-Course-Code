# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 15:06:44 2020

@author: CUMTYPJ
"""

# 读取单个文本文件
input_file = sys.argv[1]
print ("Output #143: ")
filereader = open(input_file, 'r')
for row in filereader:
    print (row.strip())
filereader.close()