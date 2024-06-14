# Код для работы с Google Sheets API



# Привет, меня зовут Рубен. Я участник команды 12524 Sputnik Original
# И так понятно зачем ты тут и для чего
# Я всего лишь хочу сказать, что ознакомится с первоисточником можно по ссылкам ниже 
# Если вы решили пользоваться данным репозиторием или приложением, то сообщите нам
# Почта: sputnik@lab244.ru или ТГ: @Ruben_Agasyan


[Как читать Google Sheet с помощью Сервисного Аккаунта](https://youtu.be/hMl-0yiBMNs).

Подробно о типах ключей в Google API (как их создавать и в чем разница) 
я рассказывал в видео:
[Как создать проект в Google Cloud Platform](https://www.youtube.com/watch?v=WpB42nS1uWE)

### Полезные ссылки

- https://console.cloud.google.com/
- https://github.com/googleapis/google-api-python-client#installation

- https://developers.google.com/sheets/api/guides/concepts
- https://developers.google.com/sheets/api/quickstart/python
- https://developers.google.com/sheets/api/guides/authorizing

### Установка
См прошлые видео в [Плейлисте Google API](https://www.youtube.com/watch?v=PjKMDtLuKPU&list=PLWVnIRD69wY4ane3amNJSFQfls1inhaub)
Но в целом, скорее всего, достаточно: 
`pip install -r req.txt`
Потом создаю Проект в Google Cloud Platform и получи Сервисный Аккаунт
Скачай в папку `creds` файлик json с секретками и назови его `sacc1.json`
Также потом пригодится api_kei в `cred/__init__.py` (см. видео)
Затем расшарь свою таблицу в Google Sheets для емейла созданноего Сервисного Аккаунта с правами Редактор