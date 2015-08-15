from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<img_id>[0-9]+)/$', views.feed, name='feed'),
    url(r'^warn/$', views.warn, name='warn'),
]
