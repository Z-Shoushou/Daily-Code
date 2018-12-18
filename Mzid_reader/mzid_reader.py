#!/usr/bin/python
# -*- coding:utf-8 -*- 

import csv

mod_rank = {}
file_name = "Fetal_Heartcombined_fdr_peptide_threshold_coord-1.2.mzid"

def mzid_reader(file_name):
    mod_rank = rank_get(file_name)
    mod_hash = seq_get(file_name)
    result_write(mod_rank,mod_hash)

def rank_get(file_name) :
    with open(file_name, 'r') as f:
        for line in f:
            if "<SpectrumIdentificationIte" in line:
                # Gain the rank information where the line head is "<SpectrumIdentificationIte "
                temp_line = line.lstrip()
                temp_line = temp_line.replace('<', '')
                temp_line = temp_line.replace(">", '')
                temp_line = temp_line.replace('\n', '')
                temp_line = temp_line.replace('\r', '')
                temp_line = temp_line.split(" ")
                for tag in temp_line:
                    tag = tag.split("=")
                    if tag[0] == "peptide_ref":
                        peptide_ref = tag[1].replace("\"", "")
                    if tag[0] == "rank":
                        rank = tag[1]
                mod_rank[peptide_ref] = rank
        return mod_rank

def seq_get(file_name) :
    mod_hash = {}
    with open(file_name, 'r') as f:
        hit = 0
        for line in f:
            if "<Peptide " in line:
                # Gain the information where the line head is "<Peptide "
                uni_mod = []
                temp_line = line.replace('><', ' ')
                temp_line = temp_line.replace("/>", '')
                temp_line = temp_line.replace(">", '')
                temp_line = temp_line.replace('\n', '')
                temp_line = temp_line.replace('\r', '')
                temp_line = temp_line.split(" ")
                for tag in temp_line:
                    tag = tag.split("=")
                    if tag[0] == "id":
                        id = tag[1].split(">")[0].replace("\"", "")
                hit = 1

            if hit == 1:
                temp_line = line.replace("/>", '')
                temp_line = temp_line.replace(">", '')
                temp_line = temp_line.replace('\n', '')
                temp_line = temp_line.split(" ")
                for tag in temp_line:
                    tag = tag.split("=")
                    if tag[0] == "accession" and ("MOD" in tag[1]):
                        tag[1] = tag[1].split(">")[0].replace("\"", "")
                        mass = tag[1]
                        if {"mass": mass} not in uni_mod:
                            uni_mod.append(mass)

            if "/Peptide>" in line:
                if uni_mod == []:
                    uni_mod.append("")
                    mod_hash[id] = uni_mod
                else:
                    mod_hash[id] = uni_mod
                hit = 0
        return mod_hash


def result_write(mod_rank,mod_hash):
    with open("result.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Title", "Sequence", "Modification"])
        for key in mod_rank:
            for key1 in mod_hash:
                if str(key) == str(key1):
                    info = []
                    mod = []
                    title = file_name + ";" + "rank=" + str(mod_rank[key]).replace("\"", "")
                    key = key.split("##")
                    seq = key[0].replace("_", "")
                    if len(key) == 1:
                        modification = ""
                        mod.append(modification)
                    elif len(key) > 1:
                        key.pop(0)
                        for i in range(len(mod_hash[key1])):
                            num = key[i].split(":")[1]
                            modification = str(num) + "-" + mod_hash[key1][i]
                            mod.append(modification)
                    Mod = str(mod).replace("[", "").replace("]", "").replace(",", ";")
                    Mod = Mod.replace("\'", "").replace(" ","")
                    info.append(title)
                    info.append(seq)
                    info.append(Mod)
                    writer.writerow(info)


if __name__ == '__main__':
    mzid_reader(file_name)
