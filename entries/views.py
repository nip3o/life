from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from entries.models import LifeEntry


@login_required
def index(request):
    e = LifeEntry.get_entries()
    return render(request, 'index.html', {"entries": e})
