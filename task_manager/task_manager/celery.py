from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите модуль настроек Django по умолчанию для программы 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')

app = Celery('task_manager')

# Используйте строку здесь, чтобы не сериализовать объект приложения Django.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Загрузите модули задач из всех зарегистрированных приложений Django.
app.autodiscover_tasks()
