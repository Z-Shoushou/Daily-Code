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

parameter = r"ascp -QT -l 500m -P33001 -i C:/Users/Shoushou/ssh.ssh/asperaweb_id_dsa.openssh"
Store_address = "C:/Users/Shoushou/biostar/aspera/"
DownloadLink = []
cmd = []

def project_judge(arguments):
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
    url = number_handling(project_number)
    print("Beginning download the project " + url[-9:] + " file.")
    folder = url[-9:]
    mkpath = Store_address + folder
    mkdir(mkpath)
    DownloadLink = get_link(url)
    cmd = tansform(DownloadLink,folder)
    command_download(cmd)
    print("Project " + url[-9:] + " download has been finished.")

def file_handling (project_file):
    # Handling the url when got a project number file
    project_list = []
    with open(project_file) as f:
        for line in f:
            list = line.split(',')
            for i in range(len(list)):
                url = 'https://www.ebi.ac.uk/pride/ws/archive/file/list/project/' + str(list[i])
                project_list.append(url)
    return project_list

def file_download(project_file) :
    urls = file_handling(project_file)
    for i in range(len(urls)):
        print("Beginning download the project " + urls[i][-9:] + " file.")
        folder = urls[i][-10:]
        mkpath = Store_address+ folder
        mkdir(mkpath)
        DownloadLink = get_link(urls[i])
        cmd = tansform(DownloadLink,folder)
        command_download(cmd)
        print ("Project " + urls[i][-9:] + " download has been finished.")

def mkdir(path):
    isExists = os.path.exists(path)
    if not isExists:
        print (path + ' creating successfully')
        os.makedirs(path)
        return True
    else:
        print(path + ' directory exists')
        return False

def get_link (url):
    # From the project number the user input get the download link.
    print('Handing web data and get the download link...')
    wbdata = js.loads(requests.get(url).text)
    data_1 = wbdata["list"]
    for i in range(len(data_1)) :
        type = data_1[i]['fileType']
        if type in file_type :
            DownloadLink.append(data_1[i]['asperaDownloadLink'])
    print("Web data ande download link have been handed.")
    return DownloadLink

def tansform (DownloadLink,floder):
    # Transform the link into windows cmd commend.
    print ("Getting the download command prompt...")
    for i in range(len(DownloadLink)):
        combine = parameter + " \""+ DownloadLink[i] + "\"" + " " + Store_address + str(floder)
        cmd.append(combine)
    print ("The download command prompt has been finished.")
    return cmd

def command_download (cmd) :
    for i in range(len(cmd)) :
        print (cmd[i])
        print ("Downloading project file...")
        output = os.popen(cmd[i], "r")
        note = str(output.read())
        print (note)
        if "Session Stop" in note:
            print("Stopping after 5 attempts")
            stop_after_5_attempts(cmd[i])

def stop_after_5_attempts(cmd):
    output = os.popen(cmd, "r")
    note = str(output.read())
    print(note)
    if "Session Stop" in note:
        for i in range(4):
            while "Session Stop" in note:
                try:
                    number = i + 2
                    print("Retrying the " + str(number) + " time download")
                    output = os.popen(cmd, "r")
                    note = output.read()
                    print(note)
                    if i == 3:
                        with open(Store_address + str(floder) + " Error note.txt", "w") as f:
                            f.write(cmd)
                            f.write(note)
                            f.write("\n")
                except Exception:
                    break
                break
    print ("Retry download successfully")

if __name__ == '__main__':
    arguments = docopt(__doc__)
    file_type = arguments['--type'].upper()
    print (file_type)
    project_judge(arguments)