from django.http import HttpResponse
from django.shortcuts import render
from service.models import Service

# View for the home page
def homePage(request):
    # Prepare data for the template
    data = {
        'title': 'Home Page - New',
        'name': 'Amit Bhardwaj',
        'numbers':[10,20,30,40,50],
        'object':[
        {'Name':'Amit','Phone':8303166787,'Age':22},
        {'Name':'Advik','Phone':9115206240,'Age':20},
        {'Name':'Ak','Phone':9115206240,'Age':21},
        ]
    }
    # Render the home page using 'index.html' template with data data can be pass from here by passing three parameter
    return render(request, 'index.html', data)
#first is for request second is file name that we wants to render and third is data that we want to pass from here to html templates file 

# View for the about me page
def aboutMe(request):
    # Instead of just HttpResponse, it's better to use a template if you want to make it more complex.
    return render(request,'about.html')
def contact(request):
    # Instead of just HttpResponse, it's better to use a template if you want to make it more complex.
    return render(request,'contact.html')

# Intro page
def intro(request):
    return HttpResponse('I am Advik')

# Course page
def course(request):
    return HttpResponse('Welcome to the course section')
# Course page
def card(request):
    servicesData=Service.objects.all()
    # for i in servicesData:
    #     print(i)
    #     print(i.service_icon)
    # print(serviceData)    
    data={
        'servicesData':servicesData
    }
    return render(request, 'card.html',data)

# Course details page with a dynamic courseId parameter
def courseDetails(request, courseId):
    # Assuming you will use courseId to fetch details from a database (if required)
    # For now, just return the courseId in the response
    return HttpResponse(f'Course ID: {courseId}')
