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
