import requests
from textdistance import ratcliff_obershelp

from typing import List, Tuple


def get_service_key(tgt_key: str) -> str:
    r = requests.post('https://utslogin.nlm.nih.gov/cas/v1/api-key/%s' % tgt_key,
                      data={
                          'service': 'http://umlsks.nlm.nih.gov',
                      })
    
    return r.text


def retrieve_cuis(word: str, ticket: str) -> List[Tuple[str, str]]:
    params = {
        'string': word,
        'ticket': ticket,
    }
    r = requests.get('https://uts-ws.nlm.nih.gov/rest/search/current',
                     params=params)
    dp = r.json()
    result = dp['result']
    results = result['results']
    
    pairs = []
    
    for r in results:
        cui = r['ui']
        name = r['name']
        pairs.append((cui, name))
    
    return pairs


def retrieve_cui_exact(word: str, ticket: str) -> str:
    pairs = retrieve_cuis(word, ticket)
    max_cui = None
    max_name = None
    max_score = 0
    
    for cui, name in pairs:
        if ratcliff_obershelp(word, name) > max_score:
            max_cui = cui
            max_name = name
            max_score = ratcliff_obershelp(word, name)
    
    return max_cui, max_name


def retrieve_atoms(cui: str, ticket: str) -> [str]:
    params = {
        'ticket': ticket,
        'language': 'ENG',
        'includeObsolete': True,
        'includeSuppressible': True,
        'pageSize': 100,
    }
    r = requests.get('https://uts-ws.nlm.nih.gov/rest/content/current/CUI/%s/atoms' % cui,
                     params=params)
    
    dp = r.json()
    atoms = dp['result']
    names = set([atom['name'].lower() for atom in atoms])
    # print(names)
    return names
