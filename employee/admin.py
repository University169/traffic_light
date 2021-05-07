from django.contrib import admin

# Register your models here.
from . models import Persone, Subdivision, Position


admin.site.register(Persone)
admin.site.register(Subdivision)
admin.site.register(Position)

