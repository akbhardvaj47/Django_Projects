from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("Welcome to Home Page")

def course(request):
    return HttpResponse("<h1>This is course page</h1>")

def details(request, id):  # Added 'id' to accept the slug from URL
    return HttpResponse(f'This is Details page with ID: {id}')

def about(request):
    return HttpResponse("This is the about page")  # 'about' view doesn't need an ID

def userFormGet(request):
    res=0
    try:
        if request.method=='GET':
            # n1=int(request.GET['num1'])
            # n2=int(request.GET['num2'])
            #We can use both method to get data
            a=int(request.GET.get('num1'))
            b=int(request.GET.get('num2'))
            res=a+b
    except:
        pass
    return render(request, 'userformget.html',{'out':res})

def userFormPost(request):
    result=0
    data={}
    try:
        if request.method=='POST':
            # n1=int(request.POST['num1'])
            # n2=int(request.POST['num2'])
            #We can use both method to get data
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            result=n1+n2
            data={
                'n1':n1,
                'n2':n2,
                'output':result
            }
    except:
        pass
    return render(request, 'userfrompost.html',data)