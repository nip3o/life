from django.conf.urls import patterns, include, url
from django.views.generic import DetailView

from entries.models import LifeEntry


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'entries.views.index', name='index'),

    url(r'^entries/(?P<pk>\d+)/$',
        DetailView.as_view(model=LifeEntry),
        name='entry_detail'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
