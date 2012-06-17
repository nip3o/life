from django.conf.urls import patterns, url
from django.views.generic import DetailView

from entries.models import LifeEntry

urlpatterns = patterns(
    url(r'', DetailView.as_view(model=LifeEntry)),
)
