# Тестовый проект для учеников Codium
Данный проект нацелен на обучение основам работы с Django и DRF (Django Rest Framework).
Учащиеся изучат и применят на практике такие понятия как:
* HTTP
* Rest Framework
* Model-View-Controller (MVC)
* Django ORM
* Routes
* Serialization
* Authentication
* Documentation

## Инструкции по установке и запуску:

##### Шаг 1.

Создайте виртуальное окружение. Для этого откройте в терминале вашую рабочую папку и запустите следующую команду (вместо *myenv* введите другое название папки):
```
python -m venv myenv
```

##### Шаг 2.
Активируйте виртуальное окружение командой:
### Для Windows:
```
myenv/Scripts/activate
```
### Для Linux:
```
source myenv/Scripts/activate
```

##### Шаг 3.


Скачайте зависимости из файла *requirements.txt*:
```
pip install -r requirements.txt
```
##### Шаг 4.
Проводим миграции:
```
python manage.py makemigrations
python manage.py migrate
```

##### Шаг 5.
Запускаем сервер:
```
python manage.py runserver
```