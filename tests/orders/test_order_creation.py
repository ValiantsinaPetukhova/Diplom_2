import allure
import pytest
import requests

from data import Urls, Data, ErrorMessages
from helpers import GenerateTestData


class TestOrderCreation:
    test_data = GenerateTestData()
    @allure.title('Проверка создания заказа для пользователя с авторизацией')
    def test_order_creation_with_auth(self, auth_user):
        payload = self.test_data.order_payload()
        token = auth_user.json()['accessToken']
        headers = {'authorization': token}
        response = requests.post(f'{Urls.ORDER_ENDPOINT}', data=payload, headers=headers)

        assert response.status_code == 200 and response.json()['success'] == True, \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа {response.text}"

    @allure.title('Проверка создания заказа для пользователя без авторизации')
    def test_order_creation_without_auth(self, non_auth_user):
        payload = self.test_data.order_payload()
        token = non_auth_user.json()['accessToken']
        headers = {'authorization': token}
        response = requests.post(f'{Urls.ORDER_ENDPOINT}', data=payload, headers=headers)

        assert response.status_code == 200 and response.json()['success'] == True, \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа {response.text}"

    @allure.title('Проверка создания заказа с ингридиентами')
    @pytest.mark.parametrize('bun_num, sauces_num, filling_num', Data.ingredients_number)
    def test_order_creation_with_ingredients_success(self, auth_user, bun_num, sauces_num, filling_num):
        payload = self.test_data.order_payload(bun_num, sauces_num, filling_num)
        token = auth_user.json()['accessToken']
        headers = {'authorization': token}
        response = requests.post(f'{Urls.ORDER_ENDPOINT}', data=payload, headers=headers)

        assert response.status_code == 200 and response.json()['success'] == True, \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа {response.text}"

    @allure.title('Проверка создания заказа без ингридиентов')
    def test_order_creation_without_ingredients_fail(self, auth_user):
        payload = self.test_data.order_payload(0, 0, 0)
        token = auth_user.json()['accessToken']
        headers = {'authorization': token}
        response = requests.post(f'{Urls.ORDER_ENDPOINT}', data=payload, headers=headers)

        assert response.status_code == 400 and response.json()['message'] == ErrorMessages.ORDER_WITHOUT_INGREDIENTS_400, \
            f"Ожидаемый код ошибки 400, актуальный - {response.status_code}, текст ответа {response.text}"

    @allure.title('Проверка создания заказа с неверным хешем ингредиентов')
    def test_order_creation_with_wrong_ingredients_id_fail(self, auth_user):
        payload = Data.ingredients_wrong
        token = auth_user.json()['accessToken']
        headers = {'authorization': token}
        response = requests.post(f'{Urls.ORDER_ENDPOINT}', data=payload, headers=headers)

        assert response.status_code == 400 and response.json()['message'] == ErrorMessages.ORDER_WRONG_ID_400, \
            f"Ожидаемый код ошибки 400, актуальный - {response.status_code}, текст ответа {response.text}"


