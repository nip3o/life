#encoding: utf-8
from django.template.defaultfilters import date as _date

from django.db import models
#from taggit_autocomplete_modified.managers import TaggableManagerAutocomplete as TaggableManager
from taggit.managers import TaggableManager

class LifeEntry(models.Model):
    class Meta:
        verbose_name = "inlägg"
        verbose_name_plural = verbose_name

    date_written = models.DateTimeField(auto_now_add = True)
    about_date = models.DateField()

    title = models.CharField(max_length=100)
    text = models.TextField()
    tags = TaggableManager()

    def __unicode__(self):
        return "%s - %s" % (_date(self.about_date, "j b"), self.title)

    @staticmethod
    def get_entries():
        return LifeEntry.objects.all().order_by('-about_date')
