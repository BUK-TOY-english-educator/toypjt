from django.urls import path, include
from . import views

app_name = 'lectures'

urlpatterns = [
    # url 수정수정
    # http://{site_url}/lectures/{path 주소}
    path('', views.index, name='index'),
    path('loading/', views.loading, name='loading'),
    path('<int:video_pk>/study/', views.study, name='study'),
    path('<int:video_pk>/writing/', views.writing, name='writing'),
    path('<int:video_pk>/speaking/', views.speaking, name='speaking'),
]
