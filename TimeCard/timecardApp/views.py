from django.shortcuts import render
from .models import Timesheet


def index(request):
    latest_entry = Timesheet.objects.all()
    context = {'latest_entry': latest_entry}
    return render(request, 'timecardApp/index.html', context)
