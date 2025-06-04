from django.shortcuts import render
from django.http import HttpResponse
from news.models import News

def home_page(request):
    project = News.objects.all()
    data = {
        'project_items': project,
    }
    return render(request, 'home.html', data)

def project_details(request, slug):  # Change 'project_slug' to 'slug'
    try:
        # Fetch project details based on the slug
        project_details = News.objects.get(project_slug=slug)  # Use 'slug' here
        data = {
            'project_details': project_details,
        }
        return render(request, 'project_details.html', data)
    except News.DoesNotExist:
        return HttpResponse("Project not found.", status=404)
