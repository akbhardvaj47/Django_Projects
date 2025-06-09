from django.http import HttpResponse
from django.shortcuts import render, redirect
from blogs.models import Category, Blogs
from .forms import SignupForm
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

def home(request):
    categories=Category.objects.all()
    Blogs.objects.all()
    featured_post=Blogs.objects.filter(is_featured=True,status='public')
    sample_post=Blogs.objects.filter(is_featured=False, status='public')
    # print(featured_post)
    context={
        'categories':categories,
        'featured_post':featured_post,
        'sample_post':sample_post
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'base/register.html', {'form': form})

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request, request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    else:
        form=AuthenticationForm()
    context={
        'form':form,
    }
    return render(request, 'base/login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')