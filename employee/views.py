from django.shortcuts import render

from .models import Subdivision, Position, Persone
# Create your views here.


def show_subdivisions(request):
    global subdivisions
    subdivisions = Subdivision.objects.all().filter(level__lte=5)
    return render(request, "subdivisions.html", {'subdivisions': subdivisions})