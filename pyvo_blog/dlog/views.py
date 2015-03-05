from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect, get_object_or_404
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

    return render(request, 'dlog/entry_form.html', context)


def entry_update(request, slug):
    obj = get_object_or_404(Entry, slug=slug)

    if request.POST:
        # form submitted
        form = EntryForm(data=request.POST, instance=obj)

        if form.is_valid():
            # data are valid
            obj = form.save()
            return redirect(obj)
        else:
            # data are invalid, return template with form errors
            pass

    else:
        # display empty form
        form = EntryForm(instance=obj)

    context = {
        'form': form
    }

    return render(request, 'dlog/entry_form.html', context)


def entry_delete(request, slug):
    entry = get_object_or_404(Entry, slug=slug)
    entry.delete()
    return redirect('home')


class EntryDetail(generic.DetailView):
    model = Entry
    context_object_name = 'entry'

detail = EntryDetail.as_view()
