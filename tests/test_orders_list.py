import requests
import allure
from help_data import url_create_order

@allure.description("Тестирование получения списка заказов через API")
class TestOrdersList:

    @allure.title("Проверяем получение списка заказов")
    def test_get_orders_list(self):
        with allure.step("Отправляем GET-запрос на получение списка заказов"):
            response = requests.get(url_create_order)

        with allure.step("Проверяем статус-код ответа"):
            assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}"

        with allure.step("Проверяем, что в ответе есть список заказов"):
            json_data = response.json()
            assert 'orders' in json_data, f"Ожидался ключ 'orders' в ответе, но получено: {json_data}"
            assert isinstance(json_data['orders'], list), "Поле 'orders' должно быть списком"
