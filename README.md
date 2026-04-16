Django Product Store API

Тестовое задание: backend API для магазина продуктов на Django Rest Framework.

🚀 Функционал

📂 Категории и подкатегории
Создание, редактирование, удаление через админку
Поля: name, slug, image
Подкатегории связаны с категориями
API: просмотр списка категорий с подкатегориями (с пагинацией)

📦 Продукты
CRUD через админку
Привязка к подкатегории
Поля:
name
slug
price
3 изображения (small, medium, large)
API: список продуктов с пагинацией

🛍 Корзина
Добавление товара
Удаление товара
Очистка корзины
Просмотр корзины:
список товаров
общее количество
итоговая стоимость

🔐 Авторизация
Token Authentication (DRF)
Доступ к корзине только у авторизованных пользователей

📄 Swagger документация

Доступна по адресу:

http://127.0.0.1:8000/api/docs/
🧪 Тесты

Реализованы:

GET /api/categories/
POST /api/cart/add/

⚙️ Установка и запуск
1. Клонировать репозиторий
git clone <ссылка_на_репозиторий>
cd <название_проекта>
2. Создать виртуальное окружение
python -m venv venv
venv\Scripts\activate
3. Установить зависимости
pip install -r requirements.txt
4. Применить миграции
python manage.py migrate
5. Загрузить фикстуры
python manage.py loaddata data.json
6. Создать суперпользователя
python manage.py createsuperuser
7. Запустить сервер
python manage.py runserver
🔑 Получение токена
python manage.py drf_create_token <username>

Использовать в заголовке:

Authorization: Token <your_token>

📬 Основные эндпоинты

Метод	URL	Описание

GET	/api/categories/	список категорий

GET	/api/products/	список продуктов

POST	/api/cart/add/	добавить в корзину

GET	/api/cart/	просмотр корзины

POST	/api/cart/remove/	удалить товар

POST	/api/cart/clear/	очистить корзину

POST	/api/token/	получить токен

🛠 Технологии
Python 3.10
Django
Django REST Framework
drf-spectacular (Swagger)
👨‍💻 Автор

Test backend project
