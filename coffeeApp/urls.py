from django.contrib.auth.views import LogoutView
from django.urls import path

from coffee_blog.views import HomeNews
from . import views

from .views import *
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('catalog/', views.catalog, name='catalog'),
    path('gallery/', views.gallery, name='gallery'),


]
