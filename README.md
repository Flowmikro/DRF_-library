# DRF_library
Основной фунĸционал для библиотеĸи.
Реализовано Rest API с базовым CRUD фунĸционалом
для ĸниг и авторов.  
___
# Установка
Установить репозиторий
```
git clone https://github.com/Flowmikro/DRF_library.git
```
Перейти в директорию
```
cd DRF_library
```
Построение образа
```
docker-compose build
```
Запуск контейнера
```
docker-compose up
```
Swagger документация доступна по адресу
```
http://127.0.0.1:8000/docs/
```
Команды
```
docker-compose run --rm web-app sh -c "python manage.py <команда>"
```