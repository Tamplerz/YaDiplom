# Андрей Кузнецов, 17-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data

# Тест. Успешное создание заказа и проверка его записи в БД
def test_getorder():
    response = sender_stand_request.post_new_order(data.order_body)
    trackid = response.json()['track']
    order_response = sender_stand_request.get_order(trackid, data.order_body2)
    assert order_response.status_code == 200
