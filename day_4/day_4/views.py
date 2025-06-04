from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    return render(request,'index.html')

def contact_page(request):
    return render(request,'Contact.html')

def about_page(request):
    return render(request,'About.html')

def projects_page(request):
    return render(request,'Projects.html')

def skills_page(request):
    return render(request,'skills.html')