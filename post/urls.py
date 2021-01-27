from django.urls import path, include
from . import views

app_name = 'post'

urlpatterns = [
    path('', views.home, name='home'),
    path('overview/', views.overview, name='overview')
]
