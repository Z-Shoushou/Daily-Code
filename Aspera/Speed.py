"""
Usage:
    Speed.py [-vrh] -f<Project_file>

Arguments:
    Project_file        Required project numbers file

Options:
    -h --help           show this
    -v                  verbose mode
    -q, --quite Sel     quite mode
    -r                  make report
    -f <Project_file>,--file <Project_file>              project number file
    -t <File_type>,--type <File_type>                     project file type

Example
    Information.py -f test.txt -t REASULT,OTHER
"""

from docopt import docopt
import requests
import json as js

DownloadLink = []
sum = 0

def handle(arguments) :
    project_file = arguments['--file']
    project_list = file_handling(project_file)
    for i in range(len(project_list)):
        dic,sum = get_size(project_list[i])
        print (i)
        time = sum/1.5
        # project = str(project_list[i][-9:0]) + ".txt"
        # print (project_list[i][-9:0])
        info = js.dumps(dic)
        with open("Project time.txt","a") as f :
            f.write(project_list[i][-10:])
            f.write(info + "\n")
            f.write("Estimated download time "+"%.2f" %time + "s" +"\n"+"\n")

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

def get_size (url):
    # From the project number the user input get the fiel size information.
    print('Handing web data and get the size information...')
    wbdata = js.loads(requests.get(url).text)
    data = wbdata["list"]
    dic = {}
    sum = 0
    for i in range(len(data)):
        type = data[i]['fileType']
        if type  == "RESULT":
            size = data[i]['fileSize'] / 1024 / 1024
            sum = size + sum
            dic[data[i]['fileName']] = size
    return dic,sum

if __name__ == '__main__':
    arguments = docopt(__doc__)
    handle(arguments)
