from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.contrib.auth import views as auth_views
from fortytwo_test_task import settings
admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'hello.views.contact_data', name='contacts'),
    url(r'^requests/$', 'hello.views.requests', name='requests'),

    url(r'users/logout/$', auth_views.logout,
        kwargs={'next_page': 'contacts'}, name='auth_logout'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns(
    '',
    url(r'^uploads/(?P<path>.*)$',
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
