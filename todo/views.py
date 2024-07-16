from django.http import JsonResponse
from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

class TodoListCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @method_decorator(csrf_exempt)
    @method_decorator(require_http_methods(["GET", "POST", "OPTIONS"]))
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @method_decorator(csrf_exempt)
    @method_decorator(require_http_methods(["GET", "PUT", "DELETE", "OPTIONS"]))
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, PUT, DELETE, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        return response

@require_http_methods(["GET", "OPTIONS"])
def health_check(request):
    response = JsonResponse({'status': 'ok'}, status=200)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return response
