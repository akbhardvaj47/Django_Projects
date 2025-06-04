from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms  import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout, authenticate
from .forms import RegisterForm  # Make sure this form exists and is named correctly

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registered Successfully')
            return redirect('login')
        # No redirect here — just fall through and re-render the form with errors
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username, password=password) 
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Credentials') 
    return render(request, 'accounts/login.html')      

def logout_view(request):
    logout(request)
    return redirect('login')    

# @login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')     
