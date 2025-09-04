import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../sample_ptc')))

from clients.reqres import ReqResClient

def test_get_user_success():
    user_id = 2
    user_data = ReqResClient.get_user(user_id)
    assert user_data['data']['id'] == user_id
    assert 'email' in user_data['data']
    assert 'first_name' in user_data['data']
    assert 'last_name' in user_data['data']

def test_create_user_success():
    name = "John Doe"
    job = "Software Developer"
    user_data = ReqResClient.create_user(name, job)
    assert user_data['name'] == name
    assert user_data['job'] == job
    assert 'id' in user_data
    assert 'createdAt' in user_data

def test_update_user_success():
    user_id = 2
    name = "Jane Doe"
    job = "Product Manager"
    user_data = ReqResClient.update_user(user_id, name=name, job=job)
    assert user_data['name'] == name
    assert user_data['job'] == job
    assert 'updatedAt' in user_data