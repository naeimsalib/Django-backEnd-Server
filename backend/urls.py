from django.contrib import admin
from django.urls import path, include
from todo.views import health_check
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo.urls')),
    path('', health_check, name='health_check'),
    path('api/todos/', views.todos, name='todos'),
]
