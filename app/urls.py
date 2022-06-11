from django.urls import path,include
from . import views

app_name='app'

urlpatterns=[
    path('', views.Home, name='home'),
    path('profiling/', views.profiling_attempt, name='profiling_attempt'),
]