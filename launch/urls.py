from django.conf.urls.defaults import *

urlpatterns = patterns('launch.views',
    url(r'^$', 'signup', name='launch_page'),
    url(r'^success/$', 'success', name='launch_page_success'),
    url(r'^success/(?P<requestid>[-\d]+)/$', 'success', name='launch_page_success_with_id'),
)
