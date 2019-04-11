from django.conf.urls import *

from .views import index,detail,results,vote, login_page, register_page, logout_view

app_name = 'polls'
urlpatterns = [
    url(r'^$', index),
    url(r'^(?P<poll_id>\d+)/$', detail),
    url(r'^(?P<poll_id>\d+)/results/$', results),
    url(r'^(?P<poll_id>\d+)/vote/$', vote),
    url(r'^login/$', login_page),
    url(r'^register/$', register_page),
    url(r'^logout/$', logout_view),
]


