from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^get_data/(?P<id>\d+)/$', views.get_data),
    url(r'^get_spec/(?P<id>\d+)/$', views.get_spec),
    url(r'^moduleSpecs/$', views.moduleSpecs),
    url(r'^moduleRequest/$', views.moduleRequest),
    url(r'^about/$', views.about),
    url(r'^contact/$', views.contact),
]