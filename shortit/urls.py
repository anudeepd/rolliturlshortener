from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('go', views.makeShortUrl),
    path('<str:shorturl>', views.redirectUrl),
]
