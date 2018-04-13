# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 11:26:18 2018

@author: 兽兽
"""

def Rename_seqⅡ(fasta = []):
    for index in range(len(fasta)-1) :
        name_in = fasta[index]
        fa_in = open(name_in,'r')
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
        C = fasta[-1]
        for index in range(len(fa_Name)) :
            Name = fa_Name[index]
            mark = Name.find(' ')
            fa_Name[index] = Name[:4] + C + str('%05d') % Number + Name[mark:]
            Number += 1
    
        sequences = dict()
        sequences =dict(zip(fa_Name,fa_Seq))
    
        mark = name_in.find('.')
        name_out = name_in[:mark] + '3.1' + name_in[mark:]
        fa_out = open(name_out,'w')
        for key in sequences.keys():
            fa_out.write(key + '\n' + str(sequences[key]))
    return 'The name part you wanted to change has been finished'
            
if __name__=='__main__':
    print ('This is a program to change the sequence name in the fasta file.')