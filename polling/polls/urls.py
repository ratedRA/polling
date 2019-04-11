from django.conf.urls import *

from .views import index,detail,results,vote

app_name = 'polls'
urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<poll_id>\d+)/$', detail),
    url(r'^(?P<poll_id>\d+)/results/$', results),
    url(r'^(?P<poll_id>\d+)/vote/$', vote),
]


