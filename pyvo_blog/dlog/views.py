from django.shortcuts import render
from dlog.models import Entry


def home(request):
    context = {
        'entries_list': Entry.objects.all()
    }

    return render(request, 'dlog/homepage.html', context)
