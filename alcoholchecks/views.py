from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from .models import Month
from .forms import MonthForm, InfoForm

def index(request):
    '''ホームページ'''
    return render(request, 'alcoholchecks/index.html')

@login_required
def monthes(request, user_id):
    user = User.objects.get(id=user_id)
    if request.user != user and str(request.user) != "alcohol_admin":
        raise Http404
    monthes = user.month_set.all()
    context = {'monthes':monthes, 'user':user}
    return render(request, 'alcoholchecks/monthes.html', context)

@login_required
def month(request, month_id):
    month = Month.objects.get(id=month_id)
    if month.owner != request.user and str(request.user) != "alcohol_admin":
        raise Http404
    infos = month.info_set.order_by('-date_added')
    context = {'month':month, 'infos':infos}
    return render(request, 'alcoholchecks/month.html', context)

@login_required
def new_month(request, user_id):
    '''新しい月を追加する'''
    user = User.objects.get(id=user_id)
    if user != request.user and str(request.user)!="alcohol_admin":
        raise Http404
    if request.method != 'POST':
        #空のフォーム
        form = MonthForm()
    else:
        form = MonthForm(data=request.POST)
        if form.is_valid():
            new_month = form.save(commit=False)
            new_month.owner = user
            new_month.save()
            return redirect('alcoholchecks:monthes', user_id=user_id)

    #空のフォームを表示させる
    context = {'form':form, 'user_id':user_id}
    return render(request, 'alcoholchecks/new_month.html', context)

@login_required
def new_info(request, month_id):
    month = Month.objects.get(id=month_id)
    if month.owner != request.user and str(request.user) != "alcohol_admin":
        raise Http404
        
    if request.method != 'POST':
        #フォームを生成
        form = InfoForm()
    else:
        #POSTで送信されたデータを処理
        form = InfoForm(data=request.POST)
        if form.is_valid():
            new_info = form.save(commit=False)
            new_info.month = month
            new_info.owner = month.owner
            new_info.save()
            return redirect('alcoholchecks:month', month_id=month_id)

    #空のフォームを表示させる
    context = {'month':month, 'form':form}
    return render(request, 'alcoholchecks/new_info.html', context)

@login_required
def check(request):
    if str(request.user) != "alcohol_admin":
        raise Http404
    users = User.objects.all()
    context = {'users':users}
    return render(request, 'alcoholchecks/check.html', context)
