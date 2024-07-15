from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('todo.urls')),
=======
    path('api/', include('todo.urls')),
    path('', health_check, name='health_check'),
>>>>>>> 9415a9d4694b224c7c9705863eb6170efa2bef1d
]
