import allure
import pytest
import requests

from data import Urls, ErrorMessages, Data
from helpers import GenerateTestData


class TestUserCreation:

    @allure.title('Проверка успешного создания пользователя')
    def test_create_user_success(self, generate_user_data_and_delete_user):
        response = requests.post(f'{Urls.USER_CREATION_ENDPOINT}',
                                 data=generate_user_data_and_delete_user)

        assert response.status_code == 200 and response.json()['success'] == True, \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа {response.text}"

    @allure.title('Проверка создания двух пользователей с одинаковыми данными')
    def test_create_two_users_with_the_same_data(self, generate_user_data_and_delete_user):
        # Создаем первого пользователя
        requests.post(f'{Urls.USER_CREATION_ENDPOINT}',
                      data=generate_user_data_and_delete_user)
        # Отправляем запрос повторно
        response = requests.post(f'{Urls.USER_CREATION_ENDPOINT}',
                                 data=generate_user_data_and_delete_user)

        assert response.status_code == 403 and response.json()["message"] == ErrorMessages.USER_EXIST_403, \
            f"Ожидаемый код ошибки 403, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Проверка создания пользователя без обязательного поля')
    @pytest.mark.parametrize('data_key', Data.data_keys)
    def test_create_user_without_one_field(self, data_key):
        test_data = GenerateTestData()
        user_data = test_data.create_register_information()
        # Удаляем один из ключей
        del user_data[data_key]
        # Отправляем запрос на создание пользователя
        response = requests.post(f'{Urls.USER_CREATION_ENDPOINT}',
                                 data=user_data)

        assert response.status_code == 403 and response.json()["message"] == ErrorMessages.USER_CREATION_403, \
            f"Ожидаемый код ошибки 403, актуальный - {response.status_code}, текст ответа: {response.text}"

