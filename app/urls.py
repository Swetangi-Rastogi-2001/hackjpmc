from django.urls import path,include
from . import views

app_name='app'

urlpatterns=[
    path('', views.Home, name='home'),
    path('profiling/', views.profiling_attempt, name='profiling_attempt'),
    path('male/', views.male, name='male'),
    path('female/', views.female, name='female'),
    path('male/cruthces/', views.male_cruthces, name='male_cruthces'),
    path('female/cruthces/', views.female_cruthces, name='female_cruthces'),
]