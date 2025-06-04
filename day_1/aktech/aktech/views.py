
from django.http import HttpResponse
from django.shortcuts import render

# This httpResponse is only use for show text on browser
def home_page(request):
    return HttpResponse('<b>This is Home Page</b>')

# This render is use for show a html file on render
def about_us():
    return HttpResponse("This is Home Page")

def course(request):
    return HttpResponse('There is my course')

def course_details(request,course_id):
    return HttpResponse(course_id)