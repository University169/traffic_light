from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.show_subdivisions, name='show_subdivisions'),
    url(r'^subdivisions$', views.show_subdivisions, name='show_subdivisions'),
]
