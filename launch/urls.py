from django.conf.urls.defaults import *

urlpatterns = patterns('launch.views',
    url(r'^$', 'signup', name='launch_page'),
    url(r'^thanks/$', 'success', name='launch_page_success'),
    url(r'^thanks/(?P<hash_value>[-\w]+)/$', 'success', name='launch_page_success_with_id'),
)
