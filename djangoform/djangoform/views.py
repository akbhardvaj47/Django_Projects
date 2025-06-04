from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import UserForm #this is class name

def home(request):
    return HttpResponse("This is home page Thank you")

def user_form(request):
    res=0
    fn=UserForm
    data={'fn':fn}
    try:
        if request.method=="POST":
            n1=request.POST.get('num1')
            n2=request.POST.get('num2')
            res=int(n1)+int(n2)
            data={
                'fn':UserForm,
                'output':res,
            }
        # return HttpResponseRedirect('/')
    except:
        pass
    return render(request, 'userForm.html',data)