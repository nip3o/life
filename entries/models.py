#encoding: utf-8
from django.template.defaultfilters import date as _date

from django.db import models
from taggit_autocomplete_modified.managers import TaggableManagerAutocomplete as TaggableManager

class LifeEntry(models.Model):
    class Meta:
        verbose_name = "inlägg"
        verbose_name_plural = verbose_name

    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = TaggableManager()

    def __unicode__(self):
        return "%s - %s" % (_date(self.date, "j b"), self.title)

    @staticmethod
    def get_entries():
        return LifeEntry.objects.all().order_by('-date')
