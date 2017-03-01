from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Team(models.Model):
    # necessary below
    teamName = models.CharField(max_length=25, unique=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    submitPassword = models.CharField(max_length=20)
    whetherSubmit = models.BooleanField(default=False)

    member1 = models.CharField(max_length=12)
    ID1 = models.CharField(max_length=13)
    department1 = models.CharField(max_length=25)

    member2 = models.CharField(max_length=12, blank=True)
    ID2 = models.CharField(max_length=13, blank=True)
    department2 = models.CharField(max_length=25, blank=True)

    member3 = models.CharField(max_length=12, blank=True)
    ID3 = models.CharField(max_length=13, blank=True)
    department3 = models.CharField(max_length=25, blank=True)

    member4 = models.CharField(max_length=12, blank=True)
    ID4 = models.CharField(max_length=13, blank=True)
    department4 = models.CharField(max_length=25, blank=True)

    member5 = models.CharField(max_length=12, blank=True)
    ID5 = models.CharField(max_length=13, blank=True)
    department5 = models.CharField(max_length=25, blank=True)

    #submit
    URL = models.URLField(max_length=100, blank=True)
    sharePassword = models.CharField(max_length=20, blank=True)

    def __unicode__(self):
        return self.teamName