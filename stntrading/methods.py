import requests
import json

FAILURE = {'success': False}

def request(url: str, payload: dict) -> dict:
    r = requests.get(url, params=payload)

    try:
        return json.loads(r.text)
    except ValueError:
        return {**FAILURE, 'status_code': r.status_code, 'text': r.text}

def post(url: str, payload: dict) -> dict:
    p = requests.post(url, data=payload)

    try:
        return json.loads(p.text)
    except ValueError:
        return {**FAILURE, 'status_code': p.status_code, 'text': p.text}
