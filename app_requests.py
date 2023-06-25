import pytest
from pytest_steps import test_steps
from jsonschema import validate
import json
import requests
from dotenv import load_dotenv
import os
import schemas

load_dotenv()
ROOT_URL = os.getenv('ROOT')

def send_req(session = None, method='get', endpoint="/", headers={}, params={}, data={}):

    url = ROOT_URL + endpoint

    with  session.request(method=method, url=url, headers=headers, params=params, data=data, verify=False) as response:
        return response


class TestAPI:

    @test_steps(
        'test_api'
    )
    def test_api(self):

        session = requests.session()

        # Provide
        data = '''{
            "user_type": "provider",
            "username": "bbb",
            "email": "bbb@example.com",
            "password": "Password123"
        }'''

        # /signup
        # res_data =send_req(session, method='post', endpoint='/signup', data=data)
        # assert (res_data.status_code == 200), f"Status Code validation failed for {res_data.request.url}"
        # assert validate(res_data.json(), schemas.user), \
        #     f"Schema Validation failed for {res_data.request.url}"
        
        # /login
        res_data =send_req(session, method='post', endpoint='/login', data=data)
        assert (res_data.status_code == 200), \
            f"Status Code validation failed for {res_data.request.url}"

        assert validate(res_data.json(), schemas.user) is None, \
            f"Schema Validation failed for {res_data.request.url}"
        
        # /user
        res_data =send_req(session, endpoint='/user')
        assert (res_data.status_code == 200), f"Status Code validation failed for {res_data.request.url}"
        assert validate(res_data.json(), schemas.user) is None, \
            f"Schema Validation failed for {res_data.request.url}"

        yield