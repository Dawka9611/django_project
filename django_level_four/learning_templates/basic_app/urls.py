from unicodedata import name
from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns =[
    path('', views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),

]

