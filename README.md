# Yatube api

## Описание:
Данный проект предоставляет REST API для всех моделей проекта **Yatube**. 
Вся логика API находится в приложении ***api***.  
Yatube api имеет аутентификацию по JWT-токену. У неаутентифицированных пользователей доступ к API имеется только на чтение, за исключением эндпоинта ``/follow/``, к нему имеет доступ только аутентифицированный пользователь, также аутентифицированным пользователям разрешено изменение и удаление своего контента.  
Проект предоставляет доступ через API для следующих моделей:
- Post
- Group
- Comment
- Follow  

С полным списком эндпоинтов можно ознакомиться после запуска проекта по адресу ```http://127.0.0.1:8000/redoc/```

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Practic73/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
py -m venv env
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
py -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Перейти в директорию, где находится manage.py:

```
cd yatube_api
```

Выполнить миграции:

```
py manage.py migrate
```

Запустить проект:

```
py manage.py runserver
```

## Основные использованные технологии:
- Python 3.10.5 ([документация](https://www.python.org/))  

***Веб разработка:***
- Django ver. 3.2.16 ([документация](https://www.djangoproject.com/download/))  

***REST API:***
- Django REST framework ver. 3.12.4 ([документация](https://www.django-rest-framework.org/))  

***Основные библиотеки:***  
- pytest ver. 6.2.4 ([документация](https://docs.pytest.org/en/latest/contents.html))
- django-filter ([документация](https://www.django-rest-framework.org/api-guide/filtering/#setting-filter-backends))
- djoser ([документация](https://djoser.readthedocs.io/en/latest/getting_started.html))
- Simple JWT ([документация](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/))

## Авторы:
**Ашанин Борис**  
Ссылка на гитхаб - https://github.com/Practic73
## Примеры запросов к API:

*```GET   .../api/v1/posts/```*
```
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
```
*```POST   .../api/v1/posts/```*
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

*```GET   .../api/v1/posts/{id}/```*
```
{
    "text": "string",
    "image": "string",
    "group": 0
}
```

*```DELETE   .../api/v1/posts/{id}/```*
```
{
    "detail": "Учетные данные не были предоставлены."
}
```

*```GET   .../api/v1/posts/{post_id}/comments/```*
```
[
    {
        "id": 0,
        "author": "string",
        "text": "string",
        "created": "2019-08-24T14:15:22Z",
        "post": 0
    }
]
```

*```POST   .../api/v1/posts/{post_id}/comments/```*
```
[
    {
        "text": "string"
    }
]
```

*```GET   .../api/v1/posts/{post_id}/comments/{id}/```*
```
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
```

*```GET   .../api/v1/groups/```*
```
[
    {
        "id": 0,
        "title": "string",
        "slug": "string",
        "description": "string"
    }
]
```

*```GET   .../api/v1/groups/```*
```
[
    {
        "id": 0,
        "title": "string",
        "slug": "string",
        "description": "string"
    }
]
```

*```GET   .../api/v1/groups/id/```*
```
{
    "id": 0,
    "title": "string",
    "slug": "string",
    "description": "string"
}
```

*```GET   .../api/v1/follow/```*
```
[
    {
        "user": "string",
        "following": "string"
    }
]
```

*```POST   .../api/v1/follow/```*
```
{
    "following": "string"
}
```

*```POST   .../api/v1/jwt/create/```*
```
{
    "username": "string",
    "password": "string"
}
```

*```POST   .../api/v1/jwt/refresh/```*
```
{
    "refresh": "string"
}
```

*```POST   .../api/v1/jwt/verify/```*
```
{
    "token": "string"
}
```