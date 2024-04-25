import allure
import requests

from data import Urls
from helpers import GenerateTestData


class TestGetUserOrders:
    test_data = GenerateTestData()
    @allure.title('Проверка получения заказов для пользователя с авторизацией')
    def test_get_user_orders_with_authorization(self, auth_user):
        payload = self.test_data.order_payload()
        token = auth_user.json()['accessToken']
        headers = {'authorization': token}
        order_response = requests.post(f'{Urls.ORDER_ENDPOINT}', data=payload, headers=headers)

        response = requests.get(f'{Urls.ORDER_ENDPOINT}', headers=headers)
        assert (response.status_code == 200 and
                order_response.json()["order"]["number"] == response.json()["orders"][0]["number"]), \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа {response.text}"

    @allure.title('Проверка получения заказов для пользователя без авторизации')
    def test_get_user_orders_without_authorization(self, non_auth_user):
        payload = self.test_data.order_payload()
        token = non_auth_user.json()['accessToken']
        headers = {'authorization': token}
        order_response = requests.post(f'{Urls.ORDER_ENDPOINT}', data=payload, headers=headers)

        response = requests.get(f'{Urls.ORDER_ENDPOINT}', headers=headers)
        assert (response.status_code == 200 and
                order_response.json()["order"]["number"] == response.json()["orders"][0]["number"]), \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа {response.text}"
