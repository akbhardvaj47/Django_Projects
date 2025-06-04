from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    data={}
    if request.method=='GET':
        num1=int(request.GET.get('num1'))
        num2=int(request.GET.get('num2'))
        res=num1+num2
        data={
            'title':'django-form',
            'num1':num1,
            'num2':num2,
            'res':res,
        }
    return render(request, 'index.html',data)

def about(request):
    return HttpResponse('<h1> Hello World about page </h1>')