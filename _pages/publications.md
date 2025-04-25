---
permalink: /publications
title: "Publications"
excerpt: ""
author_profile: true
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}


**📝 Publications** 
 
 <a href='https://scholar.google.com/citations?user=YXUc9QMAAAAJ'><img src="https://img.shields.io/badge/Citations-0-brightgreen" alt="Google Scholar Citations"></a>
 <a href='https://scholar.google.com/citations?user=YXUc9QMAAAAJ'><img src="https://img.shields.io/endpoint?url={{url|url_encode}}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=Citations"></a>
 <a href='https://scholar.google.com/citations?user=YXUc9QMAAAAJ'><img src="https://img.shields.io/badge/Citations-{{ message }}-brightgreen"></a>

<script>
  // 假设你可以从 JSON 文件加载数据
  fetch('https://raw.githubusercontent.com/jianbinwang1996/jianbinwang1996.github.io/google-scholar-stats/gs_data_shieldsio.json')
    .then(response => response.json())
    .then(data => {
      const citations = data.message;  // 获取引用数
      document.getElementById('citations-badge').src = `https://img.shields.io/badge/Citations-${citations}-brightgreen`;
    });
</script>


**📖 Collaborations**

**2024**


**2023**


**2022**
