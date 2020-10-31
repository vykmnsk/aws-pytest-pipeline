import os
import requests
import json
import pytest
from pytest_bdd import scenarios, given, when, then, parsers

URL = "https://8dpkztfg57.execute-api.ap-southeast-2.amazonaws.com/test"


@pytest.fixture
def auth_header():
    api_key = os.environ['API_KEY']
    return {'x-api-key': api_key}

def test_forbidden_without_auth():
    resp = requests.get(URL, verify=False)
    assert resp.status_code == 403
    json_content = json.loads(resp.content)
    assert json_content['message'] == 'Forbidden'
    
def test_contain_3_pets(auth_header):
    resp = requests.get(f'{URL}/pets', headers=auth_header, verify=False)
    assert resp.status_code == 200
    json_content = json.loads(resp.content)
    assert len(json_content) == 3

def test_post_call(auth_header):
    data = {"type": "Test",  "price": "23"}
    resp = requests.post(URL, data, headers=auth_header, verify=False)
    json_content = json.loads(resp.content)
    assert json_content['message'] == 'success'
    