import json
import pprint
from googleapiclient.discovery import build

my_api_key = ''
my_cse_id = '0b6f46ef574bad847'
my_search_topic = 'bootstrap'

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, start=0, **kwargs).execute()
    return res['items']

if __name__ == '__main__':
    resultsList = [11]
    i = 1
    while i < 11:
        results = google_search(my_search_topic, my_api_key, my_cse_id, num=i)
        resultsList.append(results)
        with open('google_search.json', 'w') as f:
            json.dump(results, f)
        i+=1
    pprint.pprint(resultsList) 
