# coding:utf-8
from django import forms
import re
from models import Team
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.core.validators import EmailValidator, MinLengthValidator

def validate_member_name(name):
    '''判断队员名字只能为中文'''
    name_re = re.compile(u'[\u4e00-\u9fa5]+$')
    if not re.match(name_re, name):
        raise ValidationError('请输入正确的名字')

def validate_id(id):
    '''判断学号输入是否正确'''
    if not (re.match(r'[0-9]+$',id)):
        raise ValidationError('请输入正确的学号')

def validate_phone(phone):
    pattern =re.compile(r"^1[34578]\d{9}$")
    if not re.match(pattern, phone):
        raise ValidationError('请填正确的手机号！')
class submitForm(forms.Form):


    teamName = forms.CharField(label='队伍名称', max_length=10)
    phone = forms.CharField(label='联系方式', max_length=11,
                            validators=[validate_phone])
    email = forms.CharField(label='联系邮箱',
                            max_length=25,
                            validators=[EmailValidator('请输入正确的邮箱!')])
    submitPassword = forms.CharField(label='提交密码',
                                     max_length=20,
                                     widget=forms.PasswordInput(),
                                     validators=[MinLengthValidator(6, '密码长度至少为六')]
                                     )

    member1 = forms.CharField(label='姓名', max_length=9, validators=[validate_member_name])
    ID1 = forms.CharField(label='学号', max_length=13, validators=[validate_id])

    member2 = forms.CharField(label='姓名', max_length=9,required= False, validators=[validate_member_name])
    ID2 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])

    member3 = forms.CharField(label='姓名', max_length=9,required= False, validators=[validate_member_name])
    ID3 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])

    member4 = forms.CharField(label='姓名', max_length=9,required= False, validators=[validate_member_name])
    ID4 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])

    member5 = forms.CharField(label='姓名', max_length=9,required= False, validators=[validate_member_name])
    ID5 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])

    def clean_teamName(self):
        teamName = self.cleaned_data['teamName']
        pattern = re.compile(u'[\u4e00-\u9fa5a-zA-Z0-9]+$')
        if not re.match(pattern, teamName):
            raise forms.ValidationError('不能含有特殊符号')
        try:
            Team.objects.get(teamName=teamName)
        except ObjectDoesNotExist:
            return teamName
        raise forms.ValidationError('该队名已经被使用')



