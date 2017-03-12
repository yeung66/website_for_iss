#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from models import Team, Time, Message
from form import submitForm
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime


# Create your views here.
time1 = Time.objects.get(type='软件创意大赛')
time2 = Time.objects.get(type='手机编程大赛')
time3 = Time.objects.get(type='马拉松')

def index(request):
    return render(request, 'index.html')

def intro_creativity(request):
    return render(request, 'Creativity.html')

def intro_mobile(request):
    return render(request, 'Mobile-coding.html')

def intro_hack(request):
    return render(request, 'Hackathon.html')

def notice_crea(request):
    message = Message.objects.filter(type='软件创意大赛')
    return render(request, 'Notice1.html',{'msg':message})

def notice_mobile(request):
    message = Message.objects.filter(type='手机编程大赛')
    return render(request, "Notice2.html",{'msg':message})

def notice_hack(request):
    message = Message.objects.filter(type='马拉松')
    return render(request, 'Notice3.html',{'msg':message})


def signup_crea(request):
    start_time = datetime.strptime(time1.signup_start,'%Y-%m-%d')
    end_time = datetime.strptime(time2.signup_end,'%Y-%m-%d')
    if (start_time>datetime.now()) or (datetime.now()>end_time):
        return JsonResponse({'msg':'当前不在报名时间内'})

    form = submitForm(request.POST)
    department = {}
    for i in range(1,6):
        if not request.POST.get('department'+str(i)+'_text'):
            department['department'+str(i)]=request.POST.get('department'+str(i))
        else:
            department['department'+str(i)]=request.POST.get('department'+str(i)+'_text')
    if form.is_valid():
        team = Team.objects.create(
                teamName=form.cleaned_data['teamName'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                submitPassword=form.cleaned_data['submitPassword'],
                member1=form.cleaned_data['member1'],
                ID1=form.cleaned_data['ID1'],
                department1=department['department1'],
                member2=form.cleaned_data['member2'],
                ID2=form.cleaned_data['ID2'],
                department2=department['department2'],
                member3=form.cleaned_data['member3'],
                ID3=form.cleaned_data['ID3'],
                department3=department['department3'],
                member4=form.cleaned_data['member4'],
                ID4=form.cleaned_data['ID4'],
                department4=department['department4'],
                member5=form.cleaned_data['member5'],
                ID5=form.cleaned_data['ID5'],
                department5=department['department5'],
                type='软件创意大赛'
            )
        msg='报名成功'
        type='软件创意大赛'
        return JsonResponse({'msg':msg, 'type':type})
    return JsonResponse(form.errors)

def signup_shouji(request):
    start_time = datetime.strptime(time2.signup_start, '%Y-%m-%d')  # 时间为2016年3月9日0点，根据格式替换
    end_time = datetime.strptime(time2.signup_end, '%Y-%m-%d')
    if (start_time > datetime.now()) or (datetime.now() > end_time):
        return JsonResponse({'msg': '当前不在报名时间内'})

    form = submitForm(request.POST)
    department = {}
    for i in range(1, 6):
        if not request.POST.get('department' + str(i) + '_text'):
            department['department' + str(i)] = request.POST.get('department' + str(i))
        else:
            department['department' + str(i)] = request.POST.get('department' + str(i) + '_text')
    if form.is_valid():
        team = Team.objects.create(
            teamName=form.cleaned_data['teamName'],
            phone=form.cleaned_data['phone'],
            email=form.cleaned_data['email'],
            submitPassword=form.cleaned_data['submitPassword'],
            member1=form.cleaned_data['member1'],
            ID1=form.cleaned_data['ID1'],
            department1=department['department1'],
            member2=form.cleaned_data['member2'],
            ID2=form.cleaned_data['ID2'],
            department2=department['department2'],
            member3=form.cleaned_data['member3'],
            ID3=form.cleaned_data['ID3'],
            department3=department['department3'],
            member4=form.cleaned_data['member4'],
            ID4=form.cleaned_data['ID4'],
            department4=department['department4'],
            member5=form.cleaned_data['member5'],
            ID5=form.cleaned_data['ID5'],
            department5=department['department5'],
            type='手机编程大赛'
        )
        msg = '报名成功'
        type = '手机编程大赛'
        return JsonResponse({'msg': msg, 'type': type})
    return JsonResponse(form.errors)


def signup_malasong(request):
    start_time = datetime.strptime(time3.signup_start, '%Y-%m-%d')
    end_time = datetime.strptime(time3.signup_end, '%Y-%m-%d')
    if (start_time > datetime.now()) or (datetime.now() > end_time):
        return JsonResponse({'msg': '当前不在报名时间内'})

    form = submitForm(request.POST)
    department = {}
    for i in range(1, 6):
        if not request.POST.get('department' + str(i) + '_text'):
            department['department' + str(i)] = request.POST.get('department' + str(i))
        else:
            department['department' + str(i)] = request.POST.get('department' + str(i) + '_text')
    if form.is_valid():
        team = Team.objects.create(
            teamName=form.cleaned_data['teamName'],
            phone=form.cleaned_data['phone'],
            email=form.cleaned_data['email'],
            submitPassword=form.cleaned_data['submitPassword'],
            member1=form.cleaned_data['member1'],
            ID1=form.cleaned_data['ID1'],
            department1=department['department1'],
            member2=form.cleaned_data['member2'],
            ID2=form.cleaned_data['ID2'],
            department2=department['department2'],
            member3=form.cleaned_data['member3'],
            ID3=form.cleaned_data['ID3'],
            department3=department['department3'],
            member4=form.cleaned_data['member4'],
            ID4=form.cleaned_data['ID4'],
            department4=department['department4'],
            member5=form.cleaned_data['member5'],
            ID5=form.cleaned_data['ID5'],
            department5=department['department5'],
            type='马拉松'
        )
        msg = '报名成功'
        type = '马拉松'
        return JsonResponse({'msg': msg, 'type': type})
    return JsonResponse(form.errors)

def signup(request):
    form = submitForm()
    team_crea = Team.objects.filter(type='软件创意大赛')
    team_phone = Team.objects.filter(type='手机编程大赛')
    team_malasong = Team.objects.filter(type='马拉松')

    return render(request, 'signup_crea.html', {
        'form':form,
        'team_crea':team_crea,
        'team_phone':team_phone,
        'team_malasong':team_malasong
    })


def submitWork(request):
    teamName=request.POST.get('teamName2')
    password = request.POST.get('submitPassword2')
    URL = request.POST.get('URL')
    sharePassword = request.POST.get('sharePassword')
    starttime={u'软件创意大赛':time1.submit_start, u'手机编程大赛':time2.submit_start, u'马拉松':time3.submit_start}
    endtime = {u'软件创意大赛':time1.submit_end, u'手机编程大赛': time2.submit_end, u'马拉松': time3.submit_end}
    try:
        a = Team.objects.get(teamName=teamName)
        start = datetime.strptime(starttime[a.type], '%Y-%m-%d')
        end = datetime.strptime(endtime[a.type], '%Y-%m-%d')
        if (datetime.now() < start) or (datetime.now() > end):
            return JsonResponse({'msg':'不在提交时间内'})
    except ObjectDoesNotExist:
        msg = '该队伍尚未报名'
        return JsonResponse({'msg':msg})

    if a.submitPassword  != password:
        return JsonResponse({'msg':'提交密码错误'})
    Team.objects.filter(teamName=teamName).update(
        URL = URL,
        sharePassword = sharePassword,
        whetherSubmit = True
    )
    msg = '提交成功'
    type1 = a.type
    return JsonResponse({'msg':msg,'type1':type1})
