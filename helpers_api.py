import random
import string
import requests
from data import URL


def email_pass_name_random():
    def random_string():
            random_string = f'{random.randint(0, 10000)}{''.join(random.choices(string.ascii_letters, k=10))}'
            return random_string
    return {
        "email": f'{random_string()}@{random_string()}.{random_string()}'.lower(),
        "password": random_string(),
        "name": random_string()
    }

class UserApi:

    @staticmethod
    def create_user(payload):
        return requests.post(URL.BASE_URL + URL.CREATE_USER, json=payload)
    
    @staticmethod
    def delete_user(token):
        return requests.delete(URL.BASE_URL + URL.DELETE_USER, headers={"Authorization": token})