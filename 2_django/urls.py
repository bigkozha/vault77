from django.urls import path
from counter.views import counter

urlpatterns = [
    path('', counter)
]
