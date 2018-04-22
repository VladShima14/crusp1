from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.index, name='Index'),
    url(r'^(?P<pk>\d+)/$', views.portfolio, name='project_detail'),
]
