from django.urls import path
from django.http import HttpResponse
from counter.models import Counter


value = 0


def counter(request):
    instace, created = Counter.objects.get_or_create(id=1)
    instace.value += 1
    instace.save()
    return HttpResponse(f'<div id="counter">{instace.value}</div>')


urlpatterns = [
    path('', counter)
]
