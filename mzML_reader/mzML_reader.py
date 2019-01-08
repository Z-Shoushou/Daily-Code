#!/usr/bin/python
# -*- coding:utf-8 -*- 

"""
Usage:
    mzML_reader.py [-vrh] -f<Project_file>

Arguments:
    Project_number      Required input project number
    Project_file        Required project numbers file
    File_type           Required input file type

Options:
    -h --help           show this
    -v                  verbose mode
    -q, --quite Sel     quite mode
    -r                  make report
    -f <Project_file>,--file <Project_file>              project number file
    -t <File_type>,--type <File_type>                     project file type

Example
    Aspera.py -v -n PXD003452 -t REQUEST
    Aspera.py -f test.txt -t REASULT,OTHER
"""

from docopt import docopt
import pymzml
import csv


def get_info(spectrum):
    data = []
    if spectrum['ms level'] == 2:
        list_mz = []
        list_i = []
        for mz, i in spectrum.peaks('raw'):
            list_mz.append(mz)
            list_i.append(i)
        title = "spectrum=" + str(spectrum).split(" ")[5]
        data.append(title)
        data.append(spectrum["base peak m/z"])
        data.append(spectrum["base peak intensity"])
        data.append(spectrum["charge state"])
        data.append(str(list_mz).replace("[", "").replace("]", ""))
        data.append(str(list_i).replace("[", "").replace("]", ""))
        return data


def reader(file_name):
    msrun = pymzml.run.Reader(file_name)
    with open("result.csv", "a") as csvfile :
        writer = csv.writer(csvfile)
        writer.writerow(["title", "precursor_mz DOUBLE", "precursor_intens DOUBLE", "charge INTEGER",
                         "peaklist_mz LONGTEXT", "peaklist_intens LONGTEXT"])
        for spectrum in msrun:
            data = get_info(spectrum)
            if isinstance(data, list):
                writer.writerow(data)



if __name__ == '__main__':
    arguments = docopt(__doc__)
    file_name = arguments['--file'].upper()
    reader(file_name)






