"""
Usage:
    Transform_orig.py [-vrh] (-nProject_number>|-f<Project_file>)

Arguments:
    Project_number      Required input project number
    Project_file        Required project numbers file

Options:
    -h --help           show this
    -v                  verbose mode
    -q, --quite Sel     quite mode
    -r                  make report
    -n <Project_number>,--number <Project_number>        project number
    -f <Project_file>,--file <Project_file>              project number file

Example
    Transform_orig.py -v -n PXD003452
    Transform_orig.py -f test.txt
"""

import csv
from pyteomics import mgf
from docopt import docopt


def get_info(spectrum):
    params = spectrum.get('params')
    title = params.get('title')
    n = title.find("P")
    spectrumTitle = title[n:]
    id = spectrumTitle[:9]
    precursorMz = params.get('pepmass')[0]
    # if list(params)[2] not in "title,pepmass,charge,taxonomy,seq,user03,m/z array,intensity array":
    #     precursorIntens = params.get(list(params)[2])
    # else :
    precursorIntens = "0"
    CHARGE = params.get('charge')
    peaklistMz = spectrum.get('m/z array')
    peaklistIntens = spectrum.get('intensity array')
    return spectrumTitle,id,precursorMz,precursorIntens,CHARGE,peaklistMz,peaklistIntens

def get_list(spectrum):
    spectrumTitle, id, precursorMz, precursorIntens, CHARGE, peaklistMz, peaklistIntens = get_info(spectrum)
    peaklistMz = ",".join('%s' %id for id in peaklistMz)
    peaklistIntens = ",".join('%s' %id for id in peaklistIntens)
    List = []
    List.append(spectrumTitle)
    List.append(precursorMz)
    List.append(precursorIntens)
    List.append(CHARGE)
    List.append(peaklistMz)
    List.append(peaklistIntens)
    return List

def write_in (mgf_file):
    file_name = mgf_file[:-4] + ".csv"
    with open(file_name,"a",newline="") as file :
        writer = csv.writer(file)
        writer.writerow(['spectrumTitle','precursorMz','precursorIntens','charge','peaklistMz','peaklistIntens'])
        print("Handling the data...")
        for spectrum in mgf.read(mgf_file):
            List = get_list(spectrum)
            writer.writerow(List)
        print("The data had been wrote in the csv file.")

if __name__ == '__main__':
    arguments = docopt(__doc__)
    file_number = arguments['--number']
    mgf_file = arguments['--file']
    write_in(mgf_file)




