from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView

from .models import Subdivision, Position, Persone
# Create your views here.


def show_subdivisions(request):
    global subdivisions, positions,persons
    subdivisions = Subdivision.objects.all().prefetch_related('children_subdivision').filter(level__lte=5)
    positions = Position.objects.all()
    persons = Persone.objects.all()
    context = {'subdivisions': subdivisions, 'positions': positions, 'persons': persons}
    return render(request, "subdivisions.html", context)