from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MyForm

def my_form(request):
    fn = MyForm()  # Initialize form
    data = {}
    try:
        ans = 0
        num1 = request.GET.get('num1')
        num2 = request.GET.get('num2')

        # Check if both num1 and num2 are provided and can be converted to integers
        if num1 and num2:
            try:
                num1 = int(num1)
                num2 = int(num2)
                ans = num1 + num2
            except ValueError:
                ans = "Invalid input. Please enter valid numbers."
        
        # Pass the form and the answer to the template
        data = {
            'form': fn,
            'output': ans
        }

    except Exception as e:
        data['output'] = "An error occurred: " + str(e)
    
    return render(request, 'my_form.html', data)
