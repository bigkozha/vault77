from django.urls import path
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello, world!')

urlpatterns = [
    path('', hello)
]