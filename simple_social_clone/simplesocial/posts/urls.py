from django.urls import re_path
from . import views

app_name ='posts'

urlpatterns =[
    re_path('', views.PostList.as_view(), name='all'),
    re_path('new/', views.CreatePost.as_view(), name='create'),
    re_path('by/in/<str:username>/', views.UserPosts.as_view(), name='for_user'),
    re_path('by/in/<str:username>/<int:pk>', views.PostDetail.as_view(), name='single'),
    re_path('delete/<int:pk>', views.DeletePost.as_view(), name='delete'),
]