from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView

from .models import Subdivision, Position, Persone
# Create your views here.


template_name = "employee/subdivisions.html"
def show_subdivisions(request):
    global subdivisions
    global positions
    subdivisions = Subdivision.objects.all().filter(level__lte=5)
    positions = Position.objects.all()
    # print('-'*30)
    # print(subdivisions)
    # print('=' * 30)
    # print(positions)
    # print('-' * 30)
    return render(request, "subdivisions.html", {'subdivisions': subdivisions, 'positions': positions})