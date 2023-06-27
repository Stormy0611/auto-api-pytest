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

        schema_by_code = {
            200: schemas.user,
            201: schemas.user,
            422: schemas.http_validation_error
        }
        users = []

        data = '''{
            "user_type": "provider",
            "username": "Provider1",
            "email": "provider1@example.com",
            "password": "Password123"
        }'''

        print(f"==============Testing: /signup provider1=============================")
        res_data =send_req(session, method='post', endpoint='/signup', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        
        try: 
            validate(content, schema.get(status_code, "Invaild"))
            
        except Exception as err:
            print(f"Error: \n{err}")

        data = '''{
            "user_type": "provider",
            "username": "Provider2",
            "email": "provider2@example.com",
            "password": "Password123"
        }'''
        print(f"==============Testing: /signup provider2=============================")
        res_data =send_req(session, method='post', endpoint='/signup', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        schema = {
            200: schemas.user,
            201: schemas.user,
            422: schemas.http_validation_error
        }
        try: 
            validate(res_data.json(), schema.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")
        
        
        print(f"==============Testing: /login=============================")
        res_data =send_req(session, method='post', endpoint='/login', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            validate(res_data.json(), schema.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")
        
        print(f"==============Testing: /reset=============================")
        res_data =send_req(session, method='post', endpoint='/reset')
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        schema[200] = schemas.empty_response
        try: 
            validate(res_data.json(), schema.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")

        print(f"==============Testing: /logout=============================")
        res_data =send_req(session, method='post', endpoint='/logout')
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        schema[200] = schemas.empty_response
        try: 
            validate(res_data.json(), schema.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")


       