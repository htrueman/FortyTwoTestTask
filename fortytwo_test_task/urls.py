from django.conf.urls import patterns, include, url

from django.contrib import admin

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

    url(r'^requests/', RequestKeeperView.as_view(), name='requests'),
    url(r'^requests/fetching/new$', 'hello.views.check_new_requests',
        name='request-check-new'),
    url(r'^requests/fetching/get$', 'hello.views.give_new_requests',
        name='request-fetch'),

    url(r'^edit/', 'hello.views.edit_contacts', name='edit_contacts'),

    url(r'^admin/', include(admin.site.urls)),
)
