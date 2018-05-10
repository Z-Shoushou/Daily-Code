import requests
import json as js

url = 'http://www.ebi.ac.uk:80/pride/ws/archive/file/list/project/PXD000011'
wbdata_2 = js.loads(requests.get(url).text)

data_2 = wbdata_2['list']
filetype_data = []
for i in range(len(data_2)) :
    if data_2[i]['fileType'] == 'RESULT' :
        filetype_data.append(data_2[i]['downloadLink'])


