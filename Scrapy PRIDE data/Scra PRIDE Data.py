import requests
import json as js

def filtrate_ID (url) :
    print('Handing web data...')
    wbdata = js.loads(requests.get(url).text)
    data_1 = wbdata['list']
    accession_id = []
    for i in range(len(data_1)) :
        if data_1[i]['submissionType'] == 'COMPLETE' :
            accession_id.append(data_1[i]['accession'])
    print ('Completion ID filtering.')
    return (accession_id)

def filtrate_Link (accession_id) :
    print ('Selecting the FTP link...')
    with open('result.txt', 'w') as result:
        for i in range(len(accession_id)) :
            url = 'http://www.ebi.ac.uk:80/pride/ws/archive/file/list/project/'+ accession_id[i]
            linkdata = js.loads(requests.get(url).text)
            data_2 = linkdata['list']
            result.write(str(accession_id[i]) + '\n')
            for index in range(len(data_2)):
                if data_2[index]['fileType'] == 'RESULT':
                    result.write(data_2[index]['downloadLink'] + '\n')
    print ('Finished filtrate work.')

if __name__=='__main__':
    url = 'http://www.ebi.ac.uk:80/pride/ws/archive/project/list?show=1000&page=1&order=desc'
    accession_id = filtrate_ID(url)
    filtrate_Link(accession_id)