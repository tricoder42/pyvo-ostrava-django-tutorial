from django.core.urlresolvers import reverse
from django.db import models
from django.utils.timezone import now


class Entry(models.Model):
    title = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)

    annotation = models.TextField()
    content = models.TextField()

    date_created = models.DateTimeField(default=now, blank=True)
    date_published = models.DateTimeField(null=True)

    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'slug': self.slug})
