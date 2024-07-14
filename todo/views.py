from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from django.http import JsonResponse


class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

def health_check(request):
    return JsonResponse({'status': 'ok'}, status=200)
