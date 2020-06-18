from django.urls import path
from counter import views

urlpatterns = [
    path('', views.counter),
    path('increment', views.increment),
    path('decrement', views.decrement),
    path('error', views.error)
]
