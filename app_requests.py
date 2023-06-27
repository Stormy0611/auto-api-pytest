from jsonschema import validate
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


def test_api():

        session = requests.session()

        schema_by_code = {
            200: schemas.user,
            201: schemas.user,
            422: schemas.http_validation_error
        }
        user_id = ''
        listing_id = {}

        print(f"==============Testing: SIGNUP Provider2=============================")
        data = '''{
            "user_type": "provider",
            "username": "provider2",
            "email": "provider2@example.com",
            "password": "Password123"
        }'''
        res_data =send_req(session, method='post', endpoint='/signup', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            validate(content, schema_by_code.get(status_code, "Invaild"))
            user_id = content['id']
        except Exception as err:
            print(f"Error: \n{err}")
        
        print(f"==============Testing: SIGNUP User1=============================")
        data = '''{
            "user_type": "user",
            "username": "user1",
            "email": "user1@example.com",
            "password": "Password123"
        }'''
        res_data =send_req(session, method='post', endpoint='/signup', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            validate(content, schema_by_code.get(status_code, "Invaild"))
            user_id = content['id']
        except Exception as err:
            print(f"Error: \n{err}")
        print(f"==============Testing: SIGNUP User2=============================")
        data = '''{
            "user_type": "user",
            "username": "user2",
            "email": "user2@example.com",
            "password": "Password123"
        }'''
        res_data =send_req(session, method='post', endpoint='/signup', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            validate(content, schema_by_code.get(status_code, "Invaild"))
            user_id = content['id']
        except Exception as err:
            print(f"Error: \n{err}")

        print(f"==============Testing: SIGNUP Provider1=============================")
        data = '''{
            "user_type": "provider",
            "username": "provider1",
            "email": "provider1@example.com",
            "password": "Password123"
        }'''
        res_data =send_req(session, method='post', endpoint='/signup', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            validate(content, schema_by_code.get(status_code, "Invaild"))
            user_id = content['id']
        except Exception as err:
            print(f"Error: \n{err}")
        
        print(f"==============Testing: GET User=============================")
        res_data =send_req(session, method='get', endpoint='/user')
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            validate(content, schema_by_code.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")

        print(f"==============Testing: Logout=============================")
        res_data =send_req(session, method='post', endpoint='/logout')
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            schema_by_code[200] = schemas.empty_response
            validate(content, schema_by_code.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")

        print(f"==============Testing: GET User=============================")
        res_data =send_req(session, method='get', endpoint='/user')
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            schema_by_code[200] = schemas.user
            validate(content, schema_by_code.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")

        print(f"==============Testing: Provider1 Login=============================")
        data = '''{
            "username": "provider1",
            "password": "Password123"
        }'''
        res_data =send_req(session, method='post', endpoint='/login', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            schema_by_code[200] = schemas.user
            validate(content, schema_by_code.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")

        print(f"==============Testing: Get Location=============================")
        params = {
            "query": "miller house, massachusetts avenue, district of columbia"
        }
        res_data =send_req(session, method='get', endpoint='/location', params=params)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            schema_by_code[200] = schemas.get_all_location
            validate(content, schema_by_code.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")
        
        print(f"==============Testing: Update User=============================")
        data = '''{
            "username": "provider1_updated",
            "email": "provider1_updated@example.com",
            "user_type": "user",
            "description": "I am here to find some laundry services",
            "phone": "123456789",
            "lat" : "49.0",
            "lng" : "27.0",
            "img_url" : "https://image.com/",
        }'''
        res_data =send_req(session, method='put', endpoint='/user', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            schema_by_code[200] = schemas.user
            validate(content, schema_by_code.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")
       
        print(f"==============Testing: Create Listing=============================")
        data = '''{
            "title" : "laundry service",
            "description" : "i will laundry services",
            "appointment_per_timeslot" : 1,
            "timeslot_minutes" : 30
        }'''
        res_data =send_req(session, method='post', endpoint='/listing', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            schema_by_code[200] = schemas.listing
            validate(content, schema_by_code.get(status_code, "Invaild"))
            listing_id = {
                "id": content['id'],
                "user_id": content['user_id'],
            }
        except Exception as err:
            print(f"Error: \n{err}")

        print(f"==============Testing: Get Provider Listing=============================")
        res_data =send_req(session, method='post', endpoint='/provider/listing')
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            schema_by_code[200] = schemas.get_x_all_listing_provider
            validate(content, schema_by_code.get(status_code, "Invaild"))
            for listing in content:
                if (listing['id'] == listing_id['id']):
                    print("Listing1 is exist in Response Listing array")
        except Exception as err:
            print(f"Error: \n{err}")

        print(f"==============Testing: Create Schedule=============================")
        data = '''{
            "availability": [
                {
                    "day": 0,
                    "start" : "8:00",
                    "end" : "17:00"
                },{
                    "day": 1,
                    "start" : "9:00",
                    "end" : "17:00" 
                },{
                    "day": 2,
                    "start" : "9:00",
                    "end" : "17:00" 
                },{
                    "day": 3,
                    "start" : "9:00",
                    "end" : "17:00" 
                },{
                    "day": 4,
                    "start" : "9:00",
                    "end" : "17:00" 
                },{
                    "day": 5,
                    "start" : "9:00",
                    "end" : "19:00" 
                },{
                    "day": 6,
                    "start" : "8:00",
                    "end" : "17:00" 
                }
            ]
        }'''
        res_data =send_req(session, method='post', endpoint=f'/listing/{listing_id}/schedule', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            schema_by_code[200] = schemas.schedule
            validate(content, schema_by_code.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")

        print(f"==============Testing: Create Override=============================")
        data = '''{
            "available": 0,
            "start": "2023-04-21T12:00:00",
            "end": "2023-04-22T19:00:00"
        }'''
        res_data =send_req(session, method='post', endpoint=f'/listing/{listing_id}/schedule/override', data=data)
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            schema_by_code[200] = schemas.schedule
            validate(content, schema_by_code.get(status_code, "Invaild"))
        except Exception as err:
            print(f"Error: \n{err}")

        print(f"==============Testing: Get Schedule=============================")
        res_data =send_req(session, method='get', endpoint=f'/listing/{listing_id}/schedule')
        status_code = res_data.status_code
        content = res_data.json()
        print(f"Response status: {status_code}")
        try: 
            schema_by_code[200] = schemas.schedule
            validate(content, schema_by_code.get(status_code, "Invaild"))
            
        except Exception as err:
            print(f"Error: \n{err}")

if __name__ == "__main__":
    test_api()