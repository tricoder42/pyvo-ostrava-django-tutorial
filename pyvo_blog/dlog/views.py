from django.shortcuts import render
from django.views import generic
from dlog.models import Entry


def home(request):
    context = {
        'entries_list': Entry.objects.all()
    }

    return render(request, 'dlog/homepage.html', context)


class EntryDetail(generic.DetailView):
    model = Entry
    context_object_name = 'entry'


detail = EntryDetail.as_view()
