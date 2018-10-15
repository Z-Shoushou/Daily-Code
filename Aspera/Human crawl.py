import requests
import json as js

url = "https://www.ebi.ac.uk/pride/ws/archive/project/list?show=4000&page=0&order=desc&speciesFilter=9606"


def filtrate_ID (url):
    # Used to filter the ID of the condition in the json text ("submissionType": "COMPLETE")
    print('Handing web data...')
    wbdata = js.loads(requests.get(url).text)
    data = wbdata['list']
    for i in range(len(data)):
        if data[i]['submissionType'] == 'COMPLETE':
            complete_input(str(data[i]['accession']))
        elif data[i]['submissionType'] == 'PARTIAL' :
            partial_input(str(data[i]['accession']))
        else :
            break
    print ('Completion ID filtering.')


def complete_input (content) :
    with open ("Complete.txt", "a") as f :
        f.write(content + '\n')


def partial_input (content) :
    with open("Partial.txt", "a") as f :
        f.write(content + '\n')

filtrate_ID(url)

