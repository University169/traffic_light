from django.contrib import admin
from . models import Employee

# uncomment for add 25000 employee
# from . import add_employee

admin.site.register(Employee)