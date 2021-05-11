from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, DeleteView

from .models import Subdivision, Position, Persone
from django.db.models import Prefetch
# Create your views here.


def show_subdivisions(request):
    global subdivisions
    #subdivisions = Subdivision.objects.prefetch_related('children_subdivision')
    subdivisions = Subdivision.objects.prefetch_related(
        Prefetch('children_subdivision', Persone.objects.all().select_related('employee_position'))
    )
    # вытаскиваем все подразделения, с инфой о Персонах в каждом подразделении
    # и заодно сразу вытаскиваем employee_position всех персон
    context = {'subdivisions': subdivisions}
    return render(request, "subdivisions.html", context)