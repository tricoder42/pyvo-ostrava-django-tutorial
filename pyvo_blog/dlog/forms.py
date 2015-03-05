from django import forms
from dlog.models import Entry


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'slug', 'annotation', 'content')
