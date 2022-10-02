# **API yatube**
[Yatube](https://github.com/Stas767/hw05_final) - это социальная сеть с возможностью выкладывать посты сортируя их по группам. Есть возможность подписываться на других и следить за их постами. Для этой сети разработан API.

[Соц.сеть Yatube в интернете](http://stanislavbaldzhy.pythonanywhere.com/)
___

### **Технологии**
- Django 2.2.16
- pytest 6.2.4
- pytest-pythonpath 0.7.3
- pytest-django 4.4.0
- djangorestframework 3.12.4
- djangorestframework-simplejwt 4.7.2
- Pillow 8.3.1
- PyJWT 2.1.0
- requests 2.26.0
- djoser
___

### **Как запустить проект:**
**Клонировать репозиторий и перейти в него в командной строке:**

* `git clone https://github.com/Stas767/api_final_yatube`
* `cd api_final_yatube`
  
**Cоздать и активировать виртуальное окружение:**
* `python3 -m venv env`
* `source env/bin/activate`
  
**Установить зависимости из файла requirements.txt:**

* `python3 -m pip install --upgrade pip`
* `pip install -r requirements.txt`
  
**Выполнить миграции:**

* `python3 manage.py migrate`
  
**Запустить проект:**
* `python3 manage.py runserver`
___
### **Примеры API запросов:**
```json
 http://127.0.0.1:8000/api/v1/posts/ 
{
    "text": "string",
    "image": "string",
    "group": 0
}
Добавление новой публикации в коллекцию публикаций. Анонимные запросы запрещены.
```
___
### **Об авторе:**
Меня зовут Стас и я начинающий backend-разработчик. Я обучаюсь на курсах Я.Практикума. Сейчас вы находитесь в документации к финальному проекту по теме: "API и DRF". Проект yatube, это социальная сеть с возможностью заявить о себе всему миру=) 
В этом модуле я познакомился с django rest framework.
Узнал и самое главное понял, как работает сериалайзер, какие варианты представлений есть. Вью функции, вью классы, вьюсеты, роутеры, пермишены - для меня не просто слова, а изученные инструменты для реализации поставленных задач.
___
