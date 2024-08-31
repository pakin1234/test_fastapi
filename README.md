# FastAPI E-commerce API

## Описание

Этот проект представляет собой REST API для управления продуктами на торговой площадке. API разработан с использованием фреймворка FastAPI и позволяет пользователям добавлять, обновлять, удалять и получать информацию о продуктах, а также получать информацию о категориях и фильтровать продукты по различным параметрам.

## Стек технологий

- **Python 3.10+**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Pydantic**
- **Alembic**
- **Asyncpg**

## Установка и настройка

### Клонирование репозитория

Сначала клонируйте репозиторий к себе на компьютер:

```bash
git clone https://github.com/your_username/your_repository_name.git
cd your_repository_name
```

### Создание виртуального окружения
Созадайте и активируйте виртуальное окружение

```bash
python -m venv venv
source venv/bin/activate # для MacOS/Linux
venv\Source\activate # для Windows
```

### Установка зависимостей и библиотек
Установите все необходимые библиотеки и зависимости

```bash
pip install -r requirements.txt
```
### Настройка базы данных
Создайте базу данных в PostgreSQL и настройте файл `.env` с параметрами:

```bash
DB_HOST = localhost
DB_PORT = 5432 # default port for PostgreSQL
DB_USER = database_user
DB_NAME = database_name
DB_PASS = database_password
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/your_database_name"
```

### Запуск миграций
Сначала создайте таблицы в базе данных с помощью Alembic и запустите миграции:

```bash
alembic upgrade head
```

### Запуск приложения
Запустите файл, который автоматически запустит сервер uvicorn:

```bash
python app/main.py
```

После этого приложение будет доступно по адресу `http://127.0.0.1:8000`

## Возможности приложения и API endpoints

### Категории
- **post/categories/** - Создание новой категории
- **get/categories/** - Получение всех категорий

### Продукты
- **post/products/** - Создание нового продукта
- **get/products/** - Получение всех продуктов
- **get/products/{product_id}** - Получение продукта по ID
- **post/products/{product_id}** - Обновление данных продукта по ID
- **delete/products/{product_id}** - Удаление продукта по ID
- **get/products/filter/** - Получение продуктов по различным параметрам




