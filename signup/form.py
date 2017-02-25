# coding:utf-8
from django import forms
import re
from models import Team
from django.core.exceptions import ObjectDoesNotExist

class submitForm(forms.Form):
    teamName = forms.CharField(label='队伍名称', max_length=25)
    phone = forms.CharField(label='联系方式', max_length=11)
    email = forms.EmailField(label='联系邮箱')
    submitPassword = forms.CharField(label='提交密码', max_length=20)

    member1 = forms.CharField(label='姓名', max_length=12)
    ID1 = forms.CharField(label='学号', max_length=13)
    department1 = forms.CharField(label='院系', max_length=25)

    member2 = forms.CharField(label='姓名', max_length=12,required= False)
    ID2 = forms.CharField(label='学号', max_length=13,required= False)
    department2 = forms.CharField(label='院系', max_length=25,required= False)

    member3 = forms.CharField(label='姓名', max_length=12,required= False)
    ID3 = forms.CharField(label='学号', max_length=13,required= False)
    department3 = forms.CharField(label='院系', max_length=25,required= False)

    member4 = forms.CharField(label='姓名', max_length=12,required= False)
    ID4 = forms.CharField(label='学号', max_length=13,required= False)
    department4 = forms.CharField(label='院系', max_length=25,required= False)

    member5 = forms.CharField(label='姓名', max_length=12,required= False)
    ID5 = forms.CharField(label='学号', max_length=13,required= False)
    department5 = forms.CharField(label='院系', max_length=25,required= False)

    def clean_teamName(self):
        teamName = self.cleaned_data['teamName']
        if not re.match(r'^[\u4e00-\u9fa5a-zA-Z]+$', teamName):
            raise forms.ValidationError('队名中只能由汉字，字母,数字组成')
        try:
            Team.objects.get(teamName=teamName)
        except ObjectDoesNotExist:
            return teamName
        raise forms.ValidationError('该队名已经被使用')


