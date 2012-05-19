from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    (r'^$', 'index'),
    (r'^(?P<poll_id>\d+)/$', 'detail'),
    (r'^(?P<poll_id>\d+)/results/$',
        'results'),
    (r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
