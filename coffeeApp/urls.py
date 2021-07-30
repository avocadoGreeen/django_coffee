from django.urls import path
from . import views

from .views import *
urlpatterns = [
    path('', views.home, name="home"),
    path('catalog/', views.catalog, name='catalog'),
    path('gallery/', views.gallery, name='gallery'),
]
