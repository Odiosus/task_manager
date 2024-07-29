from django.urls import path, include
from .views import TaskViewSet, TaskSearchView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('search/', TaskSearchView.as_view(), name='task-search'),
]
