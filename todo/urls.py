from django.urls import path
from .views import TodoListCreate, TodoDetail, health_check

urlpatterns = [
    path('todos/', TodoListCreate.as_view(), name='todo_list_create'),
    path('todos/<int:pk>/', TodoDetail.as_view(), name='todo_detail'),
    path('', health_check, name='health_check'),
]
