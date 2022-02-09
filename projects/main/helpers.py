from urllib.parse import quote

import requests
from django.conf import settings
from django.utils import timezone


def update_paper(project, identifier):
    url = (
        'https://api.semanticscholar.org/graph/v1/paper/'
        + quote(identifier)
        + '?fields=title,url,citations'
    )
    headers = {}
    if settings.SEMANTICSCHOLAR_API_KEY:
        headers['X-API-Key'] = settings.SEMANTICSCHOLAR_API_KEY
    r = requests.get(url, headers=headers)
    r.raise_for_status()

    data = r.json()
    project.paper_title = data['title']
    project.paper_url = data['url']
    project.paper_citations = len(data['citations'])
    project.paper_timestamp = timezone.now()
