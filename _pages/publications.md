---
permalink: /publications
title: "Publications"
excerpt: ""
author_profile: true
---

**📝 Publications** <a href='https://scholar.google.com/citations?user=YXUc9QMAAAAJ'><img src="https://img.shields.io/badge/Citations-0-brightgreen" alt="Google Scholar Citations"></a>




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




**📖 Collaborations**

**2024**


**2023**


**2022**
