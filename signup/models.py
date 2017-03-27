#coding:utf-8
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
    type = models.CharField(max_length=20,blank=True)

    member1 = models.CharField(max_length=12)
    ID1 = models.CharField(max_length=13)
    department1 = models.CharField(max_length=25, blank=True, null=True)

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



class Time(models.Model):
    type = models.CharField(u'比赛类别',max_length=20)
    signup_start = models.CharField(u'报名开始时间',max_length=20,blank=True)
    signup_end = models.CharField(u'报名结束时间',max_length=20,blank=True)
    submit_start = models.CharField(u'提交作品开始时间',max_length=20,blank=True)
    submit_end = models.CharField(u'提交作品结束时间',max_length=20,blank=True)


    def __unicode__(self):
        return self.type

class Message(models.Model):
    choice = (
        ('软件创意大赛','软件创意大赛'),
        ('手机编程大赛', '手机编程大赛'),
        ('马拉松', '马拉松'),
    )

    type=models.CharField(choices=choice, max_length=12)
    title = models.CharField(max_length=40)
    text = models.TextField(max_length=1000)
    date = models.CharField(max_length=20)

    def __unicode__(self):
        return self.title
