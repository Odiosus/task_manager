from django.conf.locale import es
from django.db import models
from elasticsearch_dsl import Document, Text, connections
from elasticsearch_dsl.connections import connections

connections.create_connection()


class TaskDocument(Document):
    title = Text()
    description = Text()

    class Index:
        name = 'tasks'


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В очереди'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.indexing()

    def indexing(self):
        obj = TaskDocument(
            meta={'id': self.id},
            title=self.title,
            description=self.description,
        )
        obj.save(index='tasks')
        return obj.to_dict(include_meta=True)

    def delete(self, *args, **kwargs):
        es.delete(index='tasks', id=self.id)
        super().delete(*args, **kwargs)
