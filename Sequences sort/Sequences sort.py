# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 13:52:06 2018

@author: 兽兽
"""

import csv

list_file = []


def loadCSVfile(csv_name):
   with open(csv_name,'r') as csv_file :
       for each_line in csv_file.readlines() :
           mark1 = each_line.find(',')
           mark2 = each_line.find(' ')
           mark3 = each_line.find('[')
           each_line = each_line[:mark1+1] + each_line[mark2:mark3] + '\n'
           list_file.append(each_line)
   return list_file     
        
loadCSVfile('pepMatch_saliva_microbio.csv')
list_file = {}.fromkeys(list_file).keys()
list_file = sorted(list_file)

c = open('seqsort.csv','w')
writer = csv.writer(c)
for index in range(len(list_file)):
    c.write(str(list_file[index]))

