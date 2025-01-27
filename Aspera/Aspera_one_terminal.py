#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
Usage:
    Aspera.py [-vrh] (-nProject_number>|-f<Project_file>) -t<File_type>

Arguments:
    Project_number      Required input project number
    Project_file        Required project numbers file
    File_type           Required input file type

Options:
    -h --help           show this
    -v                  verbose mode
    -q, --quite Sel     quite mode
    -r                  make report
    -n <Project_number>,--number <Project_number>        project number
    -f <Project_file>,--file <Project_file>              project number file
    -t <File_type>,--type <File_type>                     project file type

Example
    Aspera.py -v -n PXD003452 -t REQUEST
    Aspera.py -f test.txt -t REASULT,OTHER
"""

from docopt import docopt
import requests
import json as js
import os
import time
import math

parameter = r"nohup /usr/zhanghf/.aspera/connect/bin/ascp -QT -l 500m -k1 -P33001 -i  /usr/zhanghf/.aspera/connect/etc/asperaweb_id_dsa.openssh"
Store_address = "./"


def project_judge(arguments):
    # Identify the project as a single or document form and implement different solutions.
    project_number = arguments['--number']
    project_file = arguments['--file']
    if type(project_number) == type("abc"):
        number_download(project_number)
    else :
        file_download(project_file)


def number_handling (project_number) :
    # Handling the url when only got one project number.
    url = 'https://www.ebi.ac.uk/pride/ws/archive/file/list/project/' + str(project_number)
    return url


def number_download(project_number):
    # Download the data when only got one project number.
    url = number_handling(project_number)
    print("Beginning download the project " + url[-9:] + " file.")
    floder = url[-9:] # Project number
    mkpath = Store_address + floder # The floder address where the file is stored
    mkdir(mkpath)
    DownloadLink,FileSize = get_link(url)
    cmd = tansform(DownloadLink,floder)
    command_download(cmd,floder,FileSize)
    print("Project " + url[-9:] + " download has been finished.")


def file_handling (project_file):
    # Handling the url when got a project number file .
    project_list = []
    with open(project_file) as f:
        for line in f:
            list = line.split('\t')
            for i in range(len(list)):
                if len(line) != 1 :
                    url = 'https://www.ebi.ac.uk/pride/ws/archive/file/list/project/' + str(list[i])
                    project_list.append(url)
    return project_list


def file_download(project_file) :
    # Download the data when only got a project number file .
    urls = file_handling(project_file)
    for i in range(len(urls)):
        print("Beginning download the project " + urls[i][-10:-1] + " file.")
        floder = urls[i][-10:-1]
        mkpath = Store_address+ floder
        mkdir(mkpath)
        DownloadLink,FileSize = get_link(urls[i])
        cmd = tansform(DownloadLink,floder)
        command_download(cmd,floder,FileSize)
        print ("Project " + urls[i][-10:-1] + " download has been finished.\n")


def mkdir(path):
    # Make the dir for each project and store the data file in it .
    isExists = os.path.exists(path)
    if not isExists:
        print (path + ' creating successfully.\n')
        os.makedirs(path)
        return True
    else:
        print(path + ' directory exists.\n')
        return False


def get_link (url):
    # From the project number the user input get the download link.
    print('Handing web data and get the download link...')
    DownloadLink = []
    FileSize=[]
    wbdata = js.loads(requests.get(url).text)
    data_1 = wbdata["list"]
    for i in range(len(data_1)) :
        type = data_1[i]['fileType']
        if type in file_type :
            DownloadLink.append(data_1[i]['asperaDownloadLink'])
            FileSize.append(data_1[i]['fileSize'])
    print("Web data ande download link have been handed.")
    return DownloadLink,FileSize


def tansform (DownloadLink,floder):
    # Transform the link into windows cmd commend.
    print ("Getting the download command prompt...")
    cmd = []
    for i in range(len(DownloadLink)):
        combine = parameter + " \""+ DownloadLink[i] + "\"" + " " + Store_address + str(floder) + " &"
        cmd.append(combine)
    print ("The download command prompt has been finished.\n")
    return cmd


def command_download (cmd, floder, FileSize) :
    # Visit the system command line use Aspera to download the data .
    for (i,j) in zip(cmd,FileSize) :
        print (i)
        size = float(j)
        print ("Estimate transmission completion in " + str(math.ceil(size/2100000)) + " seconds.(Start time : "
               + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ")")
        print ("Downloading project file...")
        output = os.popen(i, "r")
        note = str(output.read())
        if "Session Stop" in note:
            fail_judge(cmd, note, i, floder)
        else:
            print(note)


def fail_judge(cmd, note, i, floder):
    # Judge the fail reason. If no such file or directory exit then pass to download it .
    if "Session Stop  (Error: Server aborted session: No such file or directory)" in note:
        print ("Error: Server aborted session: No such file or directory")
        with open(Store_address + str(floder) + " Error note.txt", "w") as f:
            f.write(cmd)
            f.write(note)
            f.write("\n")
    elif "Session Stop" in note:
        print("Trying download the data again(A hundred times at most).")
        re_download(i, floder)


def re_download(cmd,floder):
    # When get the fail download try five times to re_download .
    print("Trying the first time re-download.")
    output = os.popen(cmd, "r")
    note = str(output.read())
    print(note)
    number = 1
    while "Session Stop" in note:
        try:
            time.sleep(40)
            number += 1
            print("Retrying the " + str(number) + " time re-download")
            output = os.popen(cmd, "r")
            note = output.read()
            print(note)
            if number == 100:
                print ("Have been retried for 100 times,re-download fail. "
                       "Fail download note had been wrote in Error note.txt")
                with open(Store_address + str(floder) + " Error note.txt", "w") as f:
                    f.write(cmd)
                    f.write(note)
                    f.write("\n")
        except Exception:
            break


if __name__ == '__main__':
    arguments = docopt(__doc__)
    file_type = arguments['--type'].upper()
    print(file_type)
    project_judge(arguments)
