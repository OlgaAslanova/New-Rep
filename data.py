# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# данные пользователя для создания нового заказа в системе
# содержат имя, фамилию, адрес заказчика, ближайшую к заказчику станцию метро, телефон заказчика,
# количество дней аренды,дату доставки,комментарий от заказчика, предпочитаемые цвета
order_body = {
    "firstName": "Aleksey",
    "lastName": "Vrazhnov",
    "address": "Tverskaya, 12",
    "metroStation": 6,
    "phone": "+7 800 355 35 35",
    "rentTime": 1,
    "deliveryDate": "2024-07-07",
    "comment": "None",
    "color": [
        "BLACK"
    ]
}

params_get = {
    "t": ""
}