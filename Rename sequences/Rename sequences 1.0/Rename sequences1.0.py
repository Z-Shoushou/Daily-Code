# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:30:36 2018

@author: 兽兽
"""

fa_in = open('oral.fasta', 'r')  #Read fastafile
fa_Name = []  #Defines a list for storing information about a sequence.
fa_Seq = [] #Define a column to define a list for storing sequences.
fa_Num = -1
for line in fa_in.readlines() :
    if line[0] == ">":  #If it is a message row, it is stored in fa_Name, otherwise it is stored in fa_Seq.
        line = line.rstrip()
        fa_Name.append(line)
        fa_Num = fa_Num + 1
        fa_Seq.append("")
    else:
        fa_Seq[fa_Num] = fa_Seq[fa_Num] + line

Number = 1
for index in range(len(fa_Name)) :
    Name = fa_Name[index]
    mark = Name.find(' ')
    fa_Name[index] = Name[:4] + 'C' + str('%05d') % Number + Name[mark:]
    Number += 1
    
sequences = dict()
sequences =dict(zip(fa_Name,fa_Seq))

fa_out = open('oral1.0.fasta','w')
for key in sequences.keys():
    fa_out.write(key + '\n' + str(sequences[key]))