from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^moduleSpecs/$', views.moduleSpecs),
    url(r'^moduleRequest/$', views.moduleRequest),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.contact),
]