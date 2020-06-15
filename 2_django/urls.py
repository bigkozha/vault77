from django.urls import path
from django.http import HttpResponse


value = 0


def counter(request):
    global value
    value += 1
    return HttpResponse(f'<div id="counter">{value}</div>')


urlpatterns = [
    path('', counter)
]
