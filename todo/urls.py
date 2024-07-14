from django.urls import path
from .views import TodoListCreate, TodoDetail

urlpatterns = [
    path('api/todos/', TodoListCreate.as_view(), name='todo_list_create'),
    path('api/todos/<int:pk>/', TodoDetail.as_view(), name='todo_detail'),
]
