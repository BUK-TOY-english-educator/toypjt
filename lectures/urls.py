from django.urls import path, include
from . import views

app_name = 'lectures'

urlpatterns = [
    # url
    # http://{site_url}/lectures/{path 주소}
    path('', views.index),
    path('loading/', views.loading),
    path('<int:video_pk>/study/', views.study),
    path('<int:video_pk>/writing/', views.writing),
    path('<int:video_pk>/speaking/', views.speaking),
]
