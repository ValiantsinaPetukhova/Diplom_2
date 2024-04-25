class Urls:
    # Базовый URL эндпоинтов API
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"

    USER_CREATION_ENDPOINT = f"{BASE_URL}/auth/register"
    USER_ENDPOINT = f"{BASE_URL}/auth/user"
    USER_LOGIN_ENDPOINT = f"{BASE_URL}/auth/login"
    ORDER_ENDPOINT = f"{BASE_URL}/orders"


class ErrorMessages:

    USER_CREATION_200 = "OK"
    USER_EXIST_403 = "User already exists"
    USER_CREATION_403 = "Email, password and name are required fields"
    USER_LOGIN_401 = "email or password are incorrect"
    USER_UPDATE_401 = "You should be authorised"
    ORDER_WITHOUT_INGREDIENTS_400 = "Ingredient ids must be provided"
    ORDER_WRONG_ID_400 = "One or more ids provided are incorrect"


class Data:
    buns_id = ('61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa6c')
    sauces_id = ('61c0c5a71d1f82001bdaaa72', '61c0c5a71d1f82001bdaaa73',
                 '61c0c5a71d1f82001bdaaa74', '61c0c5a71d1f82001bdaaa75' )
    fillings_id = ('61c0c5a71d1f82001bdaaa6f', '61c0c5a71d1f82001bdaaa70',
                      '61c0c5a71d1f82001bdaaa71','61c0c5a71d1f82001bdaaa6e',
                       '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa77',
                      '61c0c5a71d1f82001bdaaa78', '61c0c5a71d1f82001bdaaa79',
                      '61c0c5a71d1f82001bdaaa7a')
    data_keys = (("email"), ("password"), ("name"))

    ingredients_number = [(1,2,2), (1,4,9)]

    ingredients_wrong = {
        "ingredients": ["60d3b41abdacab0026a000c6", "609646e4dc916e00000b2870"]
    }





