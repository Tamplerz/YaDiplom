import configuration
import requests
import data

# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_order(data.order_body);

trackid = response.json()['track']

print(trackid)
# Получение заказа по номеру
def get_order(body):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + str(trackid),
                         json=body,
                         headers=data.headers)
response = get_order(data.order_body2);
status_code_order = response.status_code