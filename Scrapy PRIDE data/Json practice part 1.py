import requests
import json as js

url = 'http://www.ebi.ac.uk:80/pride/ws/archive/project/list?show=1000&page=0&order=desc'
wbdata_1 = js.loads(requests.get(url).text)

data_1 = wbdata_1['list']
accession_id = []
for i in range(len(data_1)) :
    if data_1[i]['submissionType'] == 'COMPLETE' :
        accession_id.append(data[i]['accession'])


















