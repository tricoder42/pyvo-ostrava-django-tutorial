from django.shortcuts import render, redirect
from django.views import generic
from dlog.forms import EntryForm
from dlog.models import Entry


def home(request):
    context = {
        'entries_list': Entry.objects.all()
    }

    return render(request, 'dlog/homepage.html', context)


def entry_create(request):
    if request.POST:
        # form submitted
        form = EntryForm(data=request.POST)

        if form.is_valid():
            # data are valid
            obj = form.save()
            return redirect(obj)
        else:
            # data are invalid, return template with form errors
            pass

    else:
        # display empty form
        form = EntryForm()

    context = {
        'form': form
    }

    return render(request, 'dlog/entry_create.html', context)


class EntryDetail(generic.DetailView):
    model = Entry
    context_object_name = 'entry'

detail = EntryDetail.as_view()
