from pathlib import Path
import json

paths = [str(x) for x in Path('./youtube_data').glob('**/*.json')]
results = []
for path in paths:
    with open(path, 'r') as f:
        data = {}
        data = json.load(f)
        # insert your code here
        for p in data['videoinfo']:
            data['videoinfo'].append('id: ' + p['id'])
            data['videoinfo'].append('title: ' + p['title'])
            data['videoinfo'].append('description: ' + p['description'])
            data['videoinfo'].append('')
            results.append(data)

with open('data_for_indexing.json', 'w') as dump_file:
    json.dump(results, dump_file)
