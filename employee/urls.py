from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_employees, name='show_employees'),
    url(r'^employees$', views.show_employees, name='show_employees'),
]
