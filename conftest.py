import pytest
import requests

from data import Urls
from helpers import GenerateTestData


@pytest.fixture
def generate_user_data_and_delete_user():
    test_data = GenerateTestData()
    user_data = test_data.create_register_information()
    yield user_data
    del user_data["name"]
    response = requests.post(f'{Urls.USER_LOGIN_ENDPOINT}', data=user_data)
    token = response.json()['accessToken']
    headers = {"Content-Type": "application/json", 'authorization': token}
    requests.delete(f'{Urls.USER_ENDPOINT}', headers=headers)

@pytest.fixture
def create_and_delete_user():
    test_data = GenerateTestData()
    user_data = test_data.create_register_information()
    response = requests.post(f'{Urls.USER_CREATION_ENDPOINT}',
                             data=user_data)
    del user_data["name"]
    yield user_data
    token = response.json()['accessToken']
    headers = {"Content-Type": "application/json", 'authorization': token}
    requests.delete(f'{Urls.USER_ENDPOINT}', headers=headers)

@pytest.fixture
def auth_user():
    test_data = GenerateTestData()
    user_data = test_data.create_register_information()
    registration_response = requests.post(f'{Urls.USER_CREATION_ENDPOINT}',
                             data=user_data)
    del user_data["name"]
    response = requests.post(f'{Urls.USER_LOGIN_ENDPOINT}', data=user_data)
    token = response.json()['accessToken']
    yield registration_response
    headers = {"Content-Type": "application/json", 'authorization': token}
    requests.delete(f'{Urls.USER_ENDPOINT}', headers=headers)

@pytest.fixture
def non_auth_user():
    test_data = GenerateTestData()
    user_data = test_data.create_register_information()
    response = requests.post(f'{Urls.USER_CREATION_ENDPOINT}',
                             data=user_data)
    token = response.json()['accessToken']
    yield response
    headers = {"Content-Type": "application/json", 'authorization': token}
    requests.delete(f'{Urls.USER_ENDPOINT}', headers=headers)
