# coding:utf-8
from django import forms
import re
from models import Team
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.validators import EmailValidator, MinLengthValidator

def validate_member_name(name):
    '''判断队员名字只能为中文'''
    name_re = re.compile(r'[^\x00-\xff]')
    if not re.match(name_re, name):
        raise ValidationError('请输入正确的名字')

def validate_id(id):
    '''判断学号输入是否正确（只能为数字且为13位）'''
    if not (len(id)==13 and re.match(r'[0-9]',id)):
        raise ValidationError('请输入正确的学号')

def validate_department(department):
    if not re.match(r'[^\x00-\xff]',department):
        raise ValidationError('请输入正确的学院')

class submitForm(forms.Form):
    teamName = forms.CharField(label='队伍名称', max_length=25)
    phone = forms.CharField(label='联系方式', max_length=11)
    email = forms.CharField(label='联系邮箱',
                            max_length=25,
                            validators=[EmailValidator('请输入正确的邮箱!')])
    submitPassword = forms.CharField(label='提交密码',
                                     max_length=20,
                                     widget=forms.PasswordInput(),
                                     validators=[MinLengthValidator(6, '为确保安全性，密码长度至少为六')]
                                     )

    member1 = forms.CharField(label='姓名', max_length=12, validators=[validate_member_name])
    ID1 = forms.CharField(label='学号', max_length=13, validators=[validate_id])
    department1 = forms.CharField(label='院系', max_length=25, validators=[validate_department])

    member2 = forms.CharField(label='姓名', max_length=12,required= False, validators=[validate_member_name])
    ID2 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])
    department2 = forms.CharField(label='院系', max_length=25,required= False, validators=[validate_department])

    member3 = forms.CharField(label='姓名', max_length=12,required= False, validators=[validate_member_name])
    ID3 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])
    department3 = forms.CharField(label='院系', max_length=25,required= False, validators=[validate_department])

    member4 = forms.CharField(label='姓名', max_length=12,required= False, validators=[validate_member_name])
    ID4 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])
    department4 = forms.CharField(label='院系', max_length=25,required= False, validators=[validate_department])

    member5 = forms.CharField(label='姓名', max_length=12,required= False, validators=[validate_member_name])
    ID5 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])
    department5 = forms.CharField(label='院系', max_length=25,required= False, validators=[validate_department])

    def clean_teamName(self):
        teamName = self.cleaned_data['teamName']
        if not re.match(r'^[\u4e00-\u9fa5a-zA-Z]+$', teamName):
            raise forms.ValidationError('队名中只能由汉字，字母,数字组成')
        try:
            Team.objects.get(teamName=teamName)
        except ObjectDoesNotExist:
            return teamName
        raise forms.ValidationError('该队名已经被使用')


