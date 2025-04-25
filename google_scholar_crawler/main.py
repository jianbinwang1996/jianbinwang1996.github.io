from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os

author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
name = author['name']
author['updated'] = str(datetime.now())
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)



pip install scholarly

import os
from scholarly import scholarly

def get_citations(scholar_id):
    try:
        author = scholarly.search_author_id(scholar_id)
        if author:
            return author['citedby']
    except Exception as e:
        print(f"Error fetching citations: {e}")
    return 0

google_scholar_id = 'YXUc9QMAAAAJ'  # Replace with your Google Scholar ID
citations = get_citations(google_scholar_id)
print(f"Citations: {citations}")

python fetch_citations.py
