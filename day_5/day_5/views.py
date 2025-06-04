from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from project.models import Project
from news.models import News
def home_page(request):
    return render(request,'index.html')

def contact_page(request):
    return render(request,'Contact.html')

def about_page(request):
    return render(request,'About.html')

def news_details(request, news_id):
    news_details = News.objects.get(id=news_id)
    data={
        'news_details':news_details,
    }
    return render(request, 'news_details.html', data)




def projects_page(request):
    projects=Project.objects.all().order_by('-project_name')[:3]
    news=News.objects.all()
    data={
        'projects':projects,
        'news':news
    }
    return render(request,'Projects.html',data)

def skills_page(request):
    return render(request,'skills.html')