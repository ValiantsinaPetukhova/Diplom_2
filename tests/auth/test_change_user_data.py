import allure
import pytest
import requests

from data import Urls, ErrorMessages
from helpers import GenerateTestData


class TestChangeUserData:
    test_data = GenerateTestData()

    @allure.title('Проверка изменения данных пользователя с авторизацией')
    @pytest.mark.parametrize('user_data', test_data.create_user_updating_info())
    def test_change_user_data_with_authorization(self, auth_user, user_data):
        token = auth_user.json()['accessToken']
        headers = {'authorization': token}

        response = requests.patch(f'{Urls.USER_ENDPOINT}', data=user_data, headers=headers)
        # Формируем ожидаемый ответ
        expected_response = self.test_data.expected_response(user_data, auth_user)

        assert response.status_code == 200 and response.json() == expected_response, \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа {response.text}"

    @allure.title('Проверка изменения данных пользователя без авторизации')
    @pytest.mark.parametrize('user_data', test_data.create_user_updating_info())
    def test_change_user_data_without_authorization(self, non_auth_user, user_data):
        # Получаем токен из ответа регистрации пользователя
        token = non_auth_user.json()['accessToken']
        headers = {'authorization': token}

        response = requests.patch(f'{Urls.USER_ENDPOINT}', data=user_data, headers=headers)
        # Формируем ожидаемый ответ
        expected_response = self.test_data.expected_response(user_data, non_auth_user)

        assert response.status_code == 200 and response.json() == expected_response, \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа {response.text}"

    @allure.title('Проверка изменения данных пользователя без токена')
    @pytest.mark.parametrize('user_data', test_data.create_user_updating_info())
    def test_change_user_data_with_wrong_token_fail(self, user_data):
        headers = {'authorization': None}
        response = requests.patch(f'{Urls.USER_ENDPOINT}', data=user_data, headers=headers)

        assert response.status_code == 401 and response.json()["message"] == ErrorMessages.USER_UPDATE_401, \
            f"Ожидаемый код ошибки 401, актуальный - {response.status_code}, текст ответа {response.text}"

