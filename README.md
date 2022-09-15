# solution_fabric_test
Запуск проекта: docker-compose up --build (доп задача)

Url: http://0.0.0.0:8000

Запросы:\
1. /add_client
   1. Метод: POST
   2. request-body: array of jsons
   3. example: ```[
    {
        "client_id": 12,
        "phone_number": "79999999999",
        "operator_code": 99,
        "tag": 0,
        "time_zone": 2
    }
]```
   4. все поля обязательны
   5. status 200 - пользователен добавлен
   6. status 400 - ошибка валидации
   7. дата в формате: %Y-%m-%dT%H:%M:%SZ
2. /delete_client/{client_id}
   1. Метод: DELETE
   2. client_id - integer
   3. status 200 - пользователен удален
   4. status 404 - пользователя нет
3. /update_client/{client_id}
   1. Метод: PUT
   2. client_id - integer
   3. request-body: json
   4. example: ```
       {
        "client_id": 12,
        "phone_number": "79999999999",
        "operator_code": 99,
       } ```
   5. можно вводить любые поля
   6. status 200 - пользователен изменен
   7. status 400 - ошибка валидации
   8. status 404 - полльзователя нет
   9. дата в формате: %Y-%m-%dT%H:%M:%SZ
4. /add_mail
   10. Метод: POST
   11. request-body: array of jsons
   12. example: ```[
    {
        "mail_id": 12412,
        "date_start": "2022-09-15T20:03:55Z",
        "text": "ляля",
        "filter": 0,
        "date_end": "2022-09-15T20:51:55Z"
    }
]```
   13. все поля обязательны
   14. status 200 - рассылка добавлена
   15. status 400 - ошибка валидации
   16. дата в формате: %Y-%m-%dT%H:%M:%SZ
5. /delete_mail/{mail_id}
   1. Метод: DELETE
   2. mail_id - integer
   3. status 200 - рассылка удалена
   4. status 404 - рассылки нет
6. /update_mail/{mail_id}
   1. Метод: PUT
   2. mail_id - integer
   3. request-body: json
   4. example: ```{
    "text": "xxxx"
}```
   5. можно вводить любые поля
   6. status 200 - рассылка изменена
   7. status 400 - ошибка валидации
   8. status 404 - рассылки нет
   9. дата в формате: %Y-%m-%dT%H:%M:%SZ  
7. /get_mail_msgs/{mail_id}
   1. Метод: GET
   2. mail_id - integer
   3. status 200 - array of jsons, response: ```[
    {
        "msg_id": 1,
        "date_send": "2022-09-15T00:00:00Z",
        "status": "cancelled",
        "mail_id": 123,
        "client_id": 3
    },
    {
        "msg_id": 2,
        "date_send": "2022-09-15T00:00:00Z",
        "status": "cancelled",
        "mail_id": 123,
        "client_id": 4
    }]```  
8. /get_mails
   1. Метод: GET
   2. status 200 - json of arrays, response: ```
   {
    "sent": [
        {
            "msg_id": 6,
            "date_send": "2022-09-15T00:00:00Z",
            "status": "sent",
            "mail_id": 123,
            "client_id": 3
        }
    ],
    "cancelled": [
        {
            "msg_id": 3,
            "date_send": "2022-09-15T00:00:00Z",
            "status": "cancelled",
            "mail_id": 123,
            "client_id": 55
        }
} ```

описание методов в формате OpenAPI находится в файле openapi_doc.yaml в корне проекта

Рассылка работает с помощью Джаноговского расписание, каждую минуту пробегается по бд и ищет подходящее время
