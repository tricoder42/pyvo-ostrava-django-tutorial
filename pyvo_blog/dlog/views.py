from django.shortcuts import render
from dlog.models import Entry


def home(request):
    context = {
        'entries_list': Entry.objects.all()
    }

    return render(request, 'dlog/homepage.html', context)


def detail(request, slug):
    try:
        entry = Entry.objects.get(slug=slug)
    except Entry.DoesNotExist:
        entry = None

    context = {
        'entry': entry,
    }

    return render(request, 'dlog/entry_detail.html', context)
