from django.shortcuts import render
# from django.http import HttpResponse
from first_app.models import  AccessRecord, User
# Create your views here.


def index(request):
    # return HttpResponse("hello world!")
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    # my_dict = {'insert_me': 'Hello i am from view.py'}
    return render(request, 'first_app\index.html', context=date_dict)
    # return render(request, 'first_app/user.html')
    # return render(request, 'first_app\index.html', context=my_dict)


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict ={'users', user_list}
    return render(request, 'first_app/user.html', context=user_dict)