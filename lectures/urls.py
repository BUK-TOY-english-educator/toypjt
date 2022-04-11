from django.urls import path, include
from . import views

app_name = 'lectures'

urlpatterns = [
    # http://page_url/lectures/*
    path('', views.index),
    path('loading/', views.loading),
    path('<int:video_pk>/study/', views.study),
    path('<int:video_pk>/writing/', views.writing),
    path('<int:video_pk>/speaking/', views.speaking),
]
