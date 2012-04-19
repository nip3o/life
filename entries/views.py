from django.shortcuts import render
from entries.models import LifeEntry

def index(request):
    e = LifeEntry.get_entries()
    return render(request, 'index.html', {"entries" : e})