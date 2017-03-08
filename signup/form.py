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
    department_choice = (
        ('',''),
        ('计算机学院', '计算机学院'),
        ('国际软件学院', '国际软件学院'),
        ('弘毅学堂', '弘毅学堂'),
        ('马克思主义学院', '马克思主义学院'),
        ('政治与公共管理学院', '政治与公共管理学院'),
        ('社会学系', '社会学系'),
        ('WTO学院', 'WTO学院'),
        ('信息管理学院','信息管理学院'),
        ('经济与管理学院', '经济与管理学院'),
        ('外国语言文学学院', '外国语言文学学院'),
        ('法学院', '法学院'),
        ('数学与统计学院', '数学与统计学院'),
        ('物理科学与技术学院', '物理科学与技术学院'),
        ('化学与分子科学学院', '化学与分子科学学院'),
        ('生命科学学院', '生命科学学院'),
        ('资源与环境科学学院', '资源与环境科学学院'),
        ('测绘学院', '测绘学院'),
        ('土木建设工程学院', '土木建设工程学院'),
        ('动力与机械学院', '动力与机械学院'),
        ('电气工程学院', '电气工程学院'),
        ('水利水电学院', '水利水电学院'),
        ('药学院', '药学院'),
        ('医学院', '医学院'),
        ('城市设计学院', '城市设计学院'),
        ('电子信息学院', '电子信息学院'),
        ('印刷与包装系', '印刷与包装系'),
        ('遥感信息工程学院', '遥感信息工程学院'),
        ('测绘遥感信息工程国重', '测绘遥感信息工程国重'),
        ('公共卫生学院', '公共卫生学院'),
        ('口腔医学院', '口腔医学院'),
        ('哲学学院', '哲学学院'),
        ('历史学院', '历史学院'),
        ('文学院', '文学院'),
        ('艺术学系', '艺术学系'),
        ('教育科学学院', '教育科学学院'),
        ('HOPE护理学院', 'HOPE护理学院'),
        ('基础医学院', '基础医学院'),
        ('新闻与传播学院', '新闻与传播学院'),
        ('第一临床学院', '第一临床学院'),
        ('继续教育学院', '继续教育学院'),
        ('医学职业技术学院', '医学职业技术学院'),
        ('第二临床学院', '第二临床学院'),

    )

    teamName = forms.CharField(label='队伍名称', max_length=25)
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

    member1 = forms.CharField(label='姓名', max_length=12, validators=[validate_member_name])
    ID1 = forms.CharField(label='学号', max_length=13, validators=[validate_id])

    member2 = forms.CharField(label='姓名', max_length=12,required= False, validators=[validate_member_name])
    ID2 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])

    member3 = forms.CharField(label='姓名', max_length=12,required= False, validators=[validate_member_name])
    ID3 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])

    member4 = forms.CharField(label='姓名', max_length=12,required= False, validators=[validate_member_name])
    ID4 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])

    member5 = forms.CharField(label='姓名', max_length=12,required= False, validators=[validate_member_name])
    ID5 = forms.CharField(label='学号', max_length=13,required= False, validators=[validate_id])

    def clean_teamName(self):
        teamName = self.cleaned_data['teamName']
        pattern = re.compile(u'[\u4e00-\u9fa5a-zA-Z0-9]+$')
        if not re.match(pattern, teamName):
            raise forms.ValidationError('只能由汉字,字母,数字组成')
        try:
            Team.objects.get(teamName=teamName)
        except ObjectDoesNotExist:
            return teamName
        raise forms.ValidationError('该队名已经被使用')

class submitWorksForm(forms.Form):
    teamName2 = forms.CharField(label='队伍名称')
    submitPassword2 = forms.CharField(label='提交密码', widget=forms.PasswordInput())
    URL = forms.CharField(label='百度云链接')
    sharePassword = forms.CharField(label='分享密码')

    def clean(self):
        teamName=self.cleaned_data['teamName']
        submitpassword = self.cleaned_data['submitPassword']
        try:
            t = Team.objects.get(teamName=teamName)
        except ObjectDoesNotExist:
            raise ValidationError('该队伍还没报名')
        if t.whetherSubmit:
            raise ValidationError('该队伍已提交')
        if t.submitPassword != submitpassword:
            raise ValidationError('密码错误')

