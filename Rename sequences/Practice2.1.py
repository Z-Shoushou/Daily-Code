# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 23:17:07 2018

@author: 兽兽
"""

with open("oral.fasta",'r') as fasta_in:
    sequences = {}
    for line in fasta_in:
        if line.startswith(">"):
            name = line.rstrip("\n") 
            sequences[name] = ""
        else:
            sequences[name] = sequences[name] + line.rstrip("\n")

for key in sequences.keys() :
    mark = key.find('')
    number = '00001'
    key= key[:4] + 'C' + str(number) + key[mark:]
    number += '1'
    
for key in sequences.keys() :
    print (key)

#fasta_out = open('oral1.0.fasta','w')
#for key in sequences.keys():
#    fasta_out.write(key + '\n' + str(sequences[key]))