# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 14:16:07 2018

@author: 兽兽
"""

import csv
import pandas

file = open('swiss prot_mouse.fasta','r')
f_name = []  # Defines a list for storing sequence names.
f_sequences = []  # Define a list for storing sequences.
f_number = -1

for line in file.readlines() :
    line = line.rstrip()
    if line[0] == '>' :  # Select the name and fill in f_name
        mark = line.rfind('|')  # Find the second | location.
        f_name1 = line[4:mark]
        f_name.append(f_name1)
        f_number += 1
        f_sequences.append("")
    else :  # Select the information and fill in f_info
        f_sequences[f_number] = f_sequences[f_number] + line
fasta = dict()
fasta = dict(zip(f_name,f_sequences))

df=pandas.read_csv('residue_mass.csv') 
residue = df.set_index('Residue_name').to_dict()['monoisotopic_mass']


def mass (f_info):
    mass = 0
    for i in f_info :
        mass += float(residue[i])
    return mass

f_mass = []
for i in fasta :
    f_mass.append(mass(fasta[i]))

f_result = dict()
f_result = dict(zip(f_name,f_mass))   
f_result.items()
    
c=open("data1.csv","w")
writer=csv.writer(c)
for key in f_result.keys():       
      c.write(key.strip() + ':' + str(f_result[key]) + '\n')