import allure
import requests

from data import Urls, ErrorMessages
from helpers import GenerateTestData


class TestUserLogin:
    @allure.title('Проверка логина под существующим пользователем')
    def test_login_existent_user(self, create_and_delete_user):
        response = requests.post(f'{Urls.USER_LOGIN_ENDPOINT}', data=create_and_delete_user)

        assert response.status_code == 200 and response.json()['success'] == True, \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа {response.text}"

    @allure.title('Проверка логина под несуществующим пользователем')
    def test_login_non_existent_user(self):
        test_data = GenerateTestData()
        user_data = test_data.create_login_information()
        response = requests.post(f'{Urls.USER_LOGIN_ENDPOINT}', data=user_data)

        assert response.status_code == 401 and response.json()["message"] == ErrorMessages.USER_LOGIN_401, \
            f"Ожидаемый код ошибки 401, актуальный - {response.status_code}, текст ответа {response.text}"
