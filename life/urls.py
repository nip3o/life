from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'entries.views.index', name='index'),
    # url(r'^life/', include('life.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

# URLs for taggit_autocomplete_modified
urlpatterns += patterns('',
    url(r'^taggit_autocomplete_modified/', include('taggit_autocomplete_modified.urls')),
)