# Transform
In order to extract the information from .mgf file and rewrite it into a csv file.


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
