import random

from faker import Faker
from data import Data


class GenerateTestData:
    faker = Faker('ru_RU')

    def create_register_information(self):
        # генерируем почту, пароль и имя
        email = self.faker.email()
        password = self.faker.password()
        name = self.faker.first_name()

        # собираем тело запроса
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

    def create_login_information(self):
        # генерируем почту и пароль
        email = self.faker.email()
        password = self.faker.password()

        # собираем тело запроса
        payload = {
            "email": email,
            "password": password
        }
        return payload

    def create_user_updating_info(self):
        # генерируем почту и имя
        email_1 = self.faker.email()
        name_1 = self.faker.first_name()
        email_2 = self.faker.email()
        name_2 = self.faker.first_name()

        payload_1 = {
            "email": email_1,
            "name": name_1
        }
        payload_2 = {"email": email_2}
        payload_3 = {"name": name_2}
        payloads = (payload_1, payload_2, payload_3)
        return payloads

    def expected_response(self, user_data, registration_response):
        expected_response = {
            "success": True,
            "user": {}
        }

        # Проверяем наличие ключа 'email' в user_data
        if 'email' not in user_data:
            expected_response['user']['email'] = registration_response.json()['user']['email']
        else:
            expected_response['user']['email'] = user_data['email']

        # Проверяем наличие ключа 'name' в user_data
        if 'name' not in user_data:
            expected_response['user']['name'] = registration_response.json()['user']['name']
        else:
            expected_response['user']['name'] = user_data['name']

        return expected_response

    def order_payload(self, bun_num=1, sauces_num=1, fillings_num=1):
        # Выбираем случайную булку из списка buns_id
        selected_bun = random.sample(Data.buns_id, k=bun_num)

        # Выбираем случайные соусы из списка sauces_id
        selected_sauces = random.sample(Data.sauces_id, k=sauces_num)

        # Выбираем случайные начинки из списка fillings_id
        selected_fillings = random.sample(Data.fillings_id, k=fillings_num)

        # Составляем пэйлоад для запроса
        payload = {
            "ingredients": [selected_bun] + selected_sauces + selected_fillings
        }

        return payload

