from django.shortcuts import render
from myapp.models import Contact

def home_page(request):
    return render(request,'index.html')

def about_page(request):
    return render(request,'about.html')

def feature_page(request):
    return render(request,'feature.html')

def team_page(request):
    return render(request,'team.html')

def menu_page(request):
    return render(request,'menu.html')

def booking_page(request):
    return render(request,'booking.html')


def contact_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # You might want to add some validation here, for example:
        if name and email and subject and message:
            obj = Contact(name=name, email=email, subject=subject, message=message)
            obj.save()
        else:
            # Handle the case where not all fields were provided (optional)
            pass
    return render(request, 'contact.html')


def blog_page(request):
    return render(request,'blog.html')
def single_page(request):
    return render(request,'single.html')