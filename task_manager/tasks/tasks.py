from celery import shared_task
import time


@shared_task
def process_task(task_id):
    from .models import Task
    task = Task.objects.get(id=task_id)
    time.sleep(10)  # Ожидание 10 секунд
    task.status = 'completed'
    task.save()
