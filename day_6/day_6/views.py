from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect # use to redirect to another page
from service.models import Project
 
def home_page(request):
    return render(request,'index.html')

def contact_page(request):
    if request.method=='GET':
        ans = request.GET.get('output')  # Get the output from the URL query parameter
    return render(request, 'Contact.html', {'output': ans})

def about_page(request):
    return render(request,'About.html')

def projects_page(request):
    projects=Project.objects.all()
    return render(request,'Projects.html',{'data':projects})

def skills_page(request):
    return render(request,'skills.html')

def submit_form(request):
    output = None
    error = None
    num1 = num2 = None

    # Check if the form is submitted with GET data
    if request.method == 'GET':
        try:
            # Get data from request.GET
            num1 = request.GET.get('num1')
            num2 = request.GET.get('num2')

            if num1 and num2:
                # Try converting the inputs to integers
                try:
                    num1 = int(num1)
                    num2 = int(num2)
                    output = num1 + num2  # Perform the operation
                except ValueError:
                    error = "Please enter valid numbers."
            else:
                error = "Both fields are required."

        except Exception as e:
            error = str(e)

    # Render the form with output and error messages
    return render(request, 'userForm.html', {'output': output, 'error': error, 'num1': num1, 'num2': num2})

def user_form(request):
    ans=0
    data = {}
    try:
        # Get values from the URL query parameters
        # num1 = int(request.GET['num1'])
        # num2 = int(request.GET['num2']) 
        num1 = int(request.GET.get('num1'))
        num2 = int(request.GET.get('num2')) 
        ans = num1 + num2 

        data = {
            'n1':num1,
            'n2':num2,
            'output': ans,  # Pass the result to the template
        }

    except:
        pass

    return render(request, 'userForm.html', data)

# we can also send the data to the url in post method
 
def user_form_post(request):
    ans = 0
    data = {}
    error = None
    try:
        if request.method == 'POST':
            num1 =int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            ans=num1+num2
            data={
                'n1':num1,
                'n2':num2,
                'output':ans,
            }
            # url='/contact/?output={}'.format(ans)
            # we can write it as we use this type of url for taking value to the another page from url
            url = '/contact/' + f'?output={ans}'
            return HttpResponseRedirect(url)
    except:
        pass        
    return render(request, 'userFormPost. html', data)
