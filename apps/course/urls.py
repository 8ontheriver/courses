from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^submit$', views.submit),
    url(r'^courses/destroy/(?P<id>\d+)$', views.delete),
    url(r'^return$', views.back),
    url(r'^confirmdelete/(?P<id>\d+)$', views.crush),


]