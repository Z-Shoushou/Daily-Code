# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 17:28:20 2018

@author: 兽兽
"""


def fasta_split(fa_in) :  # Separate the name and sequence from the fasta file.
        fa_Name = []  # Defines a list for storing information about a sequence.
        fa_Seq = [] # Define a column to define a list for storing sequences.
        fa_Num = -1
        for line in fa_in.readlines() :
            if line[0] == ">":  # If it is a message row, it is stored in fa_Name, otherwise it is stored in fa_Seq.
               line = line.rstrip()
               fa_Name.append(line)
               fa_Num = fa_Num + 1
               fa_Seq.append("")
            else:
               fa_Seq[fa_Num] = fa_Seq[fa_Num] + line
        return fa_Name,fa_Seq


def fasta_dic(fa_Name,fa_Seq,fasta = []) : # Combines the renamed sequence name and the original sequence into a new dictionary.
    Number = 1
    C = fasta[-2]
    digit = fasta[-1]
    for index in range(len(fa_Name)) :
        Name = fa_Name[index]
        mark = Name.find(' ')
        fa_Name[index] = Name[:4] + C + str(digit) % Number + Name[mark:]
        Number += 1
    sequences = dict()
    sequences =dict(zip(fa_Name,fa_Seq))
    return sequences


def fasta_out(name_in,sequences) : # Output the dictionary to the new fasta file.
    mark = name_in.find('.')
    name_out = name_in[:mark] + '3.2' + name_in[mark:]
    fa_out = open(name_out,'w')
    for key in sequences.keys():
        fa_out.write(key + '\n' + str(sequences[key]))
    return name_out


def Rename_seqⅡ(fasta = []) :# Apply the above three functions together.
    import os
    import shutil
    os.mkdir('result_fasta')
    for index in range(len(fasta)-2) :
        name_in = fasta[index]
        fa_in = open(name_in,'r')
        fa_Name,fa_Seq = fasta_split(fa_in)
        sequences = fasta_dic(fa_Name,fa_Seq,fasta)
        name_out = fasta_out(name_in,sequences)
        shutil.move(name_out,'result_fasta')


if __name__=='__main__':
    fasta = ['oral.fasta','swiss prot_mouse.fasta', 'rename','%06d']
    Rename_seqⅡ(fasta)