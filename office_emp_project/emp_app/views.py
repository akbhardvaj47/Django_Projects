from django.shortcuts import render,redirect, get_object_or_404
from .models import Employee, Role, Department
from django.db.models import Q

# Create your views here.
def index(request):
    employee_list=Employee.objects.all()
    context={
        'employee_list':employee_list,
    }
    return render(request, 'index.html',context)


# ADD EMPLOYEE VIEW
def add_employee(request):
    departments = Department.objects.all()
    roles = Role.objects.all()

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        department_id = request.POST.get('department')
        role_id = request.POST.get('role')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')

        # Get ForeignKey objects from IDs
        department = Department.objects.get(id=department_id)
        # print(departments)
        role = Role.objects.get(id=role_id)

        # Create and save the employee
        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            department=department,
            role=role,
            salary=salary,
            bonus=bonus,
            phone=phone,
            hire_date=hire_date,
        )

        return redirect('all_employees')  # Redirect to employee list or success page

    return render(request, 'add_employee.html', {
        'departments': departments,
        'roles': roles
    })

# EMPLOYEE LIST VIEW
def employee_list(request):
    employee_list=Employee.objects.all()
    context={
        'employee_list':employee_list
    }
    return render(request, 'employee_list.html', context)


# EDIT VIEW
def edit_employee(request,id):
    employee=get_object_or_404(Employee, id=id)
    departments=Department.objects.all()
    roles=Role.objects.all()
    if request.method=='POST':
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.email = request.POST.get('email')
        employee.department_id = request.POST.get('department')
        employee.role_id = request.POST.get('role')
        employee.salary = request.POST.get('salary')
        employee.bonus = request.POST.get('bonus')
        employee.phone = request.POST.get('phone')
        employee.hire_date = request.POST.get('hire_date')
        employee.save()
        return redirect('all_employees') 
    context = {
        'employee': employee,
        'departments': departments,
        'roles': roles,
        'first_name': employee.first_name,
        'last_name': employee.last_name,
        'email': employee.email,
        'salary': employee.salary,
        'bonus': employee.bonus,
        'phone': employee.phone,
        'hire_date': employee.hire_date,
        'current_department': employee.department.id,
        'current_role': employee.role.id,
    }
    return render(request, 'edit_employee.html', context)

def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id) # we can change the right side value but left side id is store in db
    if request.method == 'POST':
        employee.delete()
    return redirect('all_employees')


# FILTER EMPLOYEE VIEW 
def filter_employee(request):
    employees = Employee.objects.all()
    # Getting values from filter_employee template

    name_query = request.GET.get('name')
    dept_id = request.GET.get('department')
    role_id = request.GET.get('role')

    # Apply filters based on user input
    if name_query:
        employees = employees.filter(
            Q(first_name__icontains=name_query) | Q(last_name__icontains=name_query)
        )
    if dept_id:
        employees = employees.filter(department_id=dept_id)
    if role_id:
        employees = employees.filter(role_id=role_id)

    context = {
        'employee_list': employees,
        'departments': Department.objects.all(),
        'roles': Role.objects.all(),
    }
    return render(request, 'filter_employee.html', context)
