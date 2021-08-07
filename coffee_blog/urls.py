from django.urls import path

from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='blog'),
    path('blog/<int:pk>', ViewNews.as_view(), name='detail_post'),
]
