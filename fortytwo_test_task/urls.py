from django.conf.urls import patterns, include, url

from django.contrib import admin

from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from apps.hello.views import RequestKeeperView
admin.autodiscover()


urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'fortytwo_test_task.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'hello.views.contact_data', name='contacts'),
    url(r'^requests/', RequestKeeperView.as_view(), name='requests'),
    url(r'^requests/fetching/new$', 'hello.views.check_new_requests',
        name='request-check-new'),
    url(r'^requests/fetching/get$', 'hello.views.give_new_requests',
        name='request-fetch'),

    url(r'users/logout/$', auth_views.logout,
        kwargs={'next_page': 'contacts'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='contacts'),
        name='registration'),
    url(r'^users/', include('registration.backends.simple.urls',
        namespace='users')),

    url(r'^admin/', include(admin.site.urls)),
)
