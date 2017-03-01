#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from models import Team
from form import submitForm, submitWorksForm
# Create your views here.
def index(request):
    teamAlreadySignedUp=Team.objects.all()
    if request.method =='POST':
        form = submitForm(request.POST)
        if form.is_valid():
            team=Team.objects.create(
                teamName=form.cleaned_data['teamName'],
                phone = form.cleaned_data['phone'],
                email = form.cleaned_data['email'],
                submitPassword=form.cleaned_data['submitPassword'],
                member1=form.cleaned_data['member1'],
                ID1=form.cleaned_data['ID1'],
                department1=form.cleaned_data['department1'],
                member2=form.cleaned_data['member2'],
                ID2=form.cleaned_data['ID2'],
                department2=form.cleaned_data['department2'],
                member3=form.cleaned_data['member3'],
                ID3=form.cleaned_data['ID3'],
                department3=form.cleaned_data['department3'],
                member4=form.cleaned_data['member4'],
                ID4=form.cleaned_data['ID4'],
                department4=form.cleaned_data['department4'],
                member5=form.cleaned_data['member5'],
                ID5=form.cleaned_data['ID5'],
                department5=form.cleaned_data['department5'],

            )
            return HttpResponse('报名成功')
    else:
        form = submitForm()
    return render(request, 'index.html', {'form':form, 'team':teamAlreadySignedUp})

def submitWork(request):
    if request.method =='POST':
        form = submitWorksForm(request.POST)
        if form.is_valid():
            teamName = form.cleaned_data['teamName']
            team = Team.objects.get(teamName=teamName)
            if form.cleaned_data['submitPassword'] != team.submitPassword:
                return HttpResponse('提交密码错误')
            else:
                Team.objects.filter(teamName=teamName).update(
                    URL=form.cleaned_data['URL'],
                    sharePassword = form.cleaned_data['sharePassword'],
                    whetherSubmit = True
                )
                return HttpResponse('提交作品成功')

    else:
        form = submitWorksForm()
    return render(request, 'submit.html', {'form':form})