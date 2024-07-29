<h1 align="center">Система управления задачами</h1>

# Обзор

Это простая система управления задачами, построенная с использованием Django и Django REST Framework. Включает в себя
функции управления задачами, асинхронной обработки задач с использованием Celery, брокера сообщений RabbitMQ,
мониторинга задач с помощью Flower и полнотекстового поиска с использованием Elasticsearch.

# Возможности

- [x] Управление задачами: создание, чтение, обновление и удаление задач.
- [x] Асинхронная обработка: задачи обрабатываются асинхронно с использованием Celery.
- [x] Полнотекстовый поиск: поиск задач по названию и описанию с помощью Elasticsearch.
- [x] Мониторинг: мониторинг задач Celery с использованием Flower.

## Стек

- Docker
- Docker Compose
- Django Web Application
- PostgreSQL (База данных)
- RabbitMQ (Брокер сообщений)
- Elasticsearch (Поисковый движок)
- Flower (Мониторинг Celery)

## Установка и настройка

### Клонирование репозитория

```bash
git clone https://github.com/Odiosus/task_manager
cd task-manager
```

### Сборка и запуск сервисов

```bash
docker-compose up --build
```

### Применение миграций

После запуска контейнеров примените миграции:

```bash
docker-compose exec web python manage.py migrate
```

### Создание суперпользователя

Чтобы создать суперпользователя для админ-панели Django

```bash
docker-compose exec web python manage.py createsuperuser
```

## Использование

### API Эндпоинты

1. Создание задачи

- Эндпоинт: `POST /api/tasks/`

```bash
curl -X POST http://localhost:8000/api/tasks/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Новая задача", "description": "Описание задачи", "status": "pending"}'
```

2. Получение списка всех задач

- Эндпоинт: `GET /api/tasks/`

```bash
curl http://localhost:8000/api/tasks/
```

3. Получение информации о задаче

- Эндпоинт: `GET /api/tasks/<task_id>/`

```bash
curl http://localhost:8000/api/tasks/1/
```

4. Обновление задачи

- Эндпоинт: `PUT /api/tasks/<task_id>/`

```bash
curl -X PUT http://localhost:8000/api/tasks/1/ \
     -H "Content-Type: application/json" \
     -d '{"title": "Обновленная задача", "description": "Обновленное описание", "status": "in_progress"}'
```

5. Удаление задачи

- Эндпоинт: `DELETE /api/tasks/<task_id>/`

```bash
curl -X DELETE http://localhost:8000/api/tasks/1/
```

### Поиск задач

Задачи можно искать по названию или описанию с помощью Elasticsearch.

- Эндпоинт: `GET /api/tasks/search/`

```bash
curl http://localhost:8000/api/tasks/search/?query=Задача
```

### Мониторинг задач Celery
Для мониторинга задач Celery используется Flower.

- Панель управления Flower: http://localhost:5555

Для доступа к панели управления Flower перейдите на http://localhost:5555 в вашем браузере.

### Переменные окружения

- DATABASE_URL: URL для подключения к базе данных PostgreSQL.
- CELERY_BROKER_URL: URL для брокера RabbitMQ.
- ELASTICSEARCH_URL: URL для сервиса Elasticsearch.


Все переменные окружения используются напрямую умышленно, поскольку версия системы упрвления задачами носит тестовый (демонстрационный) характер. 


