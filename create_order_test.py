import sender_stand_request

# Тест. Успешное создание заказа и проверка его записи в БД
def test_getorder():
    order_response = sender_stand_request.status_code_order
    assert order_response == 200