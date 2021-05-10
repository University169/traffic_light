from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView

from .models import Subdivision, Position, Persone
# Create your views here.


def show_subdivisions(request):
    global subdivisions
    subdivisions = Subdivision.objects.prefetch_related('children_subdivision')
    context = {'subdivisions': subdivisions}
    return render(request, "subdivisions.html", context)