from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views

app_name ='groups'

urlpatterns =[
    re_path('', views.ListGroups.as_view(), name='all'),
    re_path('new/', views.CreateGroup.as_view(), name='create'),
    re_path('posts/in/<str:slug>/', views.SingleGroup.as_view(), name='single'),
    re_path('join/<str:slug>/', views.JoinGroup.as_view(), name='join'),
    re_path('leave/<str:slug>/', views.LeaveGroup.as_view(), name='leave')
]