from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', views.index, name='Index'),
    url(r'^(?P<pk>\d+)/$', views.portfolio, name='project_detail'),
    url(r'^contact-send/$', views.contact_form, name="contact_form"),
]
