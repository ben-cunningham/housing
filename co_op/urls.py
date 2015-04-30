from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^$', views.landing_view),
    url(r'^postings$', views.list_view),
    url(r'^post/new/$', views.form_view, name='form_view'),
    url(r'^posts/(?P<post_id>\d+)/$', views.detail_view),
    url(r'^logout/$', views.logout),
    url(r'^history$', views.user_postings),
)

