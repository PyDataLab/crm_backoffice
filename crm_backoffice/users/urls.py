from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Этот маршрут будет отображать index.html
]
