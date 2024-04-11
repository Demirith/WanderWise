from django.urls import path
from . import views 

urlpatterns = [
    path('trips/suggestion', views.suggestion, name='suggestion'),
]