from django.shortcuts import render

from .models import Employee
# Create your views here.


def show_employees(request):
    global employees
    employees = Employee.objects.all().filter(level__lte=5)
    return render(request, "employees.html", {'employees': employees})