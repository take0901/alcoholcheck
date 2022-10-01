from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from .models import Month, Info
from .forms import MonthForm, InfoForm
import csv
import datetime

def index(request):
    '''ホームページ'''
    check = ""
    if str(request.user) == "alcohol_admin":
        check = "チェックする"
    context = {'check':check}
    return render(request, 'alcoholchecks/index.html', context)

@login_required
def monthes(request, user_id):
    user = User.objects.get(id=user_id)
    delete = ""
    if request.user != user and str(request.user) != "alcohol_admin":
        raise Http404
    if str(request.user) == "alcohol_admin":
        delete = "削除"
    monthes = user.month_set.all()
    context = {'monthes':monthes, 'user':user, 'delete':delete}
    return render(request, 'alcoholchecks/monthes.html', context)

@login_required
def month(request, month_id):
    month = Month.objects.get(id=month_id)
    delete = ""
    if month.owner != request.user and str(request.user) != "alcohol_admin":
        raise Http404
    if str(request.user) == "alcohol_admin":
        delete = "削除"
    infos = month.info_set.order_by('-date_added')
    context = {'month':month, 'infos':infos, 'delete':delete}
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

@login_required
def delete_month(request, month_id):
    #月を削除する
    month = get_object_or_404(Month, id=month_id)
    if str(request.user) != "alcohol_admin":
        raise Http404
    
    if request.method == "POST":
        month.delete()
        return redirect('alcoholchecks:monthes', user_id=month.owner.id)

    context = {'month':month}
    return render(request, 'alcoholchecks/delete_month.html', context)

@login_required
def delete_info(request, info_id):
    #記録を削除
    info = get_object_or_404(Info, id=info_id)
    month = info.month
    if str(request.user) != "alcohol_admin":
        raise Http404

    if request.method == 'POST':
        info.delete()
        return redirect('alcoholchecks:month', month_id=month.id)

    context = {'month':month, 'info':info}
    return render(request, 'alcoholchecks/delete_info.html', context)

@login_required
def download(request, user_id):
     
    user = User.objects.get(id=user_id)
    monthes = Month.objects.filter(owner=user)
    response = HttpResponse(content_type="text/csv; charset=Shift-JIS")
    response['Content-Disposition'] = 'attachment;  filename="{}_data.csv"'.format(user)
    writer = csv.writer(response)
    infolist = []
    for month in monthes:
        infos = month.info_set.all()
        infolist.extend(infos)
    
    for info in infolist:
        info.date_added += datetime.timedelta(hours=9)
        writer.writerow([info.date_added.strftime('%Y/%m/%d %H:%M')
        ,info.carnumber,info.alcohol,"武村義治"])
    return response