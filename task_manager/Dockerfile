# Используем официальный образ Python
FROM python:3.10-slim

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Установка Python-зависимостей
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код приложения
COPY . /app

# Установка переменных окружения
ENV DJANGO_SETTINGS_MODULE=task_manager.settings
ENV PYTHONUNBUFFERED=1
ENV DATABASE_URL=postgres://default:lMND5Yyec3JT@ep-rough-frog-a4k1b6r2-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require

# Открываем порт
EXPOSE 8000

# Запуск приложения
CMD ["gunicorn", "task_manager.wsgi:application", "--bind", "0.0.0.0:8000"]
