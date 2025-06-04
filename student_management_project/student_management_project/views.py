from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from student_app.models import Student

def home_page(request):
    student_data = Student.objects.all()
    paginator = Paginator(student_data, 3)
    page_number = request.GET.get('page')
    students = paginator.get_page(page_number)
    return render(request, 'index.html', {'students': students})



def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        if name and email and address and phone:
            Student.objects.create(name=name, email=email, address=address, phone=phone)
        return redirect('home')
    

def delete_student(request, student_id):
    if request.method == 'POST':
        try:
            student = Student.objects.get(id=student_id)
            student.delete()
        except Student.DoesNotExist:
            pass  

        return redirect('home') 
    return render(request, 'index.html',{'students':student})

def edit_student(request, student_id):
    if request.method == 'POST':
        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            pass  
        return redirect('home') 
    return render(request, 'index.html',{'students':student})

def update_student(request,student_id):
    if request.method == 'POST':
       student=Student.objects.get(id=student_id)
       student.name=request.POST.get('name')
       student.email=request.POST.get('email')
       student.address=request.POST.get('address')
       student.phone=request.POST.get('phone')
       student.save()
       return redirect('home')
    return render(request, 'index.html')

# def student_list(request):
#     student = Student.objects.all()
#     paginator = Paginator(student, 3)

#     page_number = request.GET.get('page')
#     students = paginator.get_page(page_number)

#     return render(request, 'index.html', {'students': students})


# def delete_student(request, student_id):
#     # if request.method == 'POST':
#     try:
#         student = Student.objects.get(id=student_id)
#         student.delete()
#     except Student.DoesNotExist:
#         pass  

#         # return redirect('home') 
#     return render(request, 'index.html',{'student':student})
