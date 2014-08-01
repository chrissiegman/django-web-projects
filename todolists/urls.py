from django.conf.urls import patterns, url

from todolists import views

urlpatterns = patterns('',
        url(r'^$', views.index, name ='index'),
        url(r'^(?P<todolist_id>\d+)/detail/$', views.detail, name='detail'),
        url(r'^(?P<todolist_id>\d+)/toggle/$', views.toggle_completion, name='toggle_completion'),
        )


