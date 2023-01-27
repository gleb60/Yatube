from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):    
    return HttpResponse('Первая и самая главная страница')

def group_posts(request, num1):
    return HttpResponse('Список групп')
