from django.contrib import admin
from django.urls import path, include
from todo.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo.urls')),
    path('', health_check, name='health_check'),
]
