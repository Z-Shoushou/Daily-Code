# Aspera download
In order to use Aspera download the PRIDE data more save both time and labour，and make the download speed more quickly.

Use Aspera.py for window .
Use Aspera_one/more.py for Linux.(If u want to download the data and when finish it and try to copy it to other load , usr Aspera_more.py,if not use Aspera_one.py)



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
