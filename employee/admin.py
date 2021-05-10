from django.contrib import admin

# Register your models here.
from . models import Persone, Subdivision, Position
from mptt.admin import MPTTModelAdmin


admin.site.register(Persone)
admin.site.register(Subdivision, MPTTModelAdmin)
admin.site.register(Position)

