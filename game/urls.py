
from django.conf.urls import url
from django.contrib.auth import views as authviews

from . import views

urlpatterns = [
    url(r'planet/(?P<method>[\w\-]+)/', views.planet, name='planet'),

]