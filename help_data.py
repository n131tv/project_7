import string
import random
import requests

base_url = 'https://qa-scooter.praktikum-services.ru'
url_create_courier = f'{base_url}/api/v1/courier'
url_courier_login = f'{base_url}/api/v1/courier/login'
url_create_order = f'{base_url}/api/v1/orders'


def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_login_password_fname():
    return {
        "login": "test_login",
        "password": "test_password",
        "first_name": "test_name"
    }

def registration_courier():
    login_pass = generate_random_login_password_fname()
    requests.post(url_create_courier, data=login_pass)
    return login_pass