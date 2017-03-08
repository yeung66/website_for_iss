#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from models import Team
from form import submitForm, submitWorksForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def index(request):
    return render(request, 'index.html')

def intro_creativity(request):
    return render(request, 'Creativity.html')

def intro_mobile(request):
    return render(request, 'Mobile-coding.html')

def intro_hack(request):
    return render(request, 'Hackathon.html')

def notice_crea(request):
    return render(request, 'Notice1.html')

def notice_mobile(request):
    return render(request, "Notice2.html")

def notice_hack(request):
    return render(request, 'Notice3.html')


def signup(request):
    teamAlreadySignedUp=Team.objects.all()
    form = submitForm()
    state = request.GET.get('state', '')

    return render(request, 'signup.html', {'form':form, 'team':teamAlreadySignedUp, 'state':state})

def signup_crea(request):
    state = request.GET.get('state', '')
    team_alreadySignup = Team.objects.filter(type='软件创意大赛')
    form_submit = submitWorksForm()
    if (request.method =='POST') & (not request.is_ajax()):
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
            return HttpResponseRedirect('/signup_crea/?state=报名成功')
    else:
        form = submitForm()
    return render(request, 'signup_crea.html', {'form':form,
                                                'state':state,
                                                'team':team_alreadySignup,
                                                'form2':form_submit})

def signup_shouji(request):
    state = request.GET.get('state', '')
    team_alreadySignup = Team.objects.filter(type='手机编程大赛')
    form_submit = submitWorksForm()
    if request.method == 'POST':
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
            return HttpResponseRedirect('/signup_shouji/?state=报名成功')
    else:
        form = submitForm()
    return render(request, 'signup_shouji.html', {'form': form,
                                                'state': state,
                                                'team': team_alreadySignup,
                                                'form2': form_submit})


def signup_malasong(request):
    state = request.GET.get('state', '')
    team_alreadySignup = Team.objects.filter(type='马拉松')
    form_submit = submitWorksForm()
    if request.method == 'POST':
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
            return HttpResponseRedirect('/signup_malasong/?state=报名成功')
    else:
        form = submitForm()
    return render(request, 'signup_malasong.html', {'form': form,
                                                  'state': state,
                                                  'team': team_alreadySignup,
                                                  'form2': form_submit})


def submitWork(request):
    teamName=request.POST.get('teamName2')
    password = request.POST.get('submitPassword2')
    URL = request.POST.get('URL')
    sharePassword = request.POST.get('sharePassword')
    try:
        a = Team.objects.get(teamName=teamName)
    except ObjectDoesNotExist:
        msg = '该队伍尚未报名'
        return HttpResponse(msg)
    if a.whetherSubmit:
        msg = '该队伍已提交，请不要重复提交'
        return HttpResponse(msg)
    if a.submitPassword  != password:
        return HttpResponse('提交密码错误')
    Team.objects.filter(teamName=teamName).update(
        URL = URL,
        sharePassword = sharePassword,
        whetherSubmit = True
    )
    msg = '提交成功'
    return HttpResponse(msg)
