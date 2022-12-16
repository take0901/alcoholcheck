from django.shortcuts import render, redirect
from .models import Information
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import InfoForm

@login_required
def infos(request):
    infos = Information.objects.all().order_by('-year', "-month")
    year_list = sorted(list(map(int,Information.objects.values_list("year", flat=True).distinct())))
    month_list = sorted(list(map(int,Information.objects.values_list("month", flat=True).distinct())))
    motouke_list = list(Information.objects.values_list("motouke", flat=True).distinct())
    year_list.insert(0,"すべての")
    month_list.insert(0,"すべての")
    motouke_list.insert(0,"すべて")
    if request.method == "POST" and request.POST.get("reset") != "reset":
        years, months, motoukes = [],[], [] 
        year = request.POST['year']
        years.append(year)
        if year == "すべての":
            years = year_list
        else:
            remove_and_insert(year_list, int(year))
        month = request.POST['month']
        months.append(month)
        if month == "すべての":
            months = month_list
        else:
            remove_and_insert(month_list, int(month))
        motouke = request.POST['motouke']
        motoukes.append(motouke)
        if motouke == "すべて": 
            motoukes = motouke_list
        remove_and_insert(motouke_list, motouke)
        infos = Information.objects.filter(year__in=years, month__in=months
        ,motouke__in=motoukes).order_by("-year", '-month')
    context = {'infos':infos, 'years':year_list, 'months':month_list, 'motoukes':motouke_list}
    return render(request, 'informations/infos.html', context)

@login_required
def new_info(request):
    if str(request.user) != "alcohol_admin":
        raise Http404
    
    if request.method != 'POST':
        #フォームを生成
        form = InfoForm()
    else:
        #POSTで送信されたデータを処理
        form = InfoForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('informations:infos')
    context = {'form':form}
    return render(request, 'informations/new_info.html', context)

@login_required
def edit_info(request, info_id):
    info = Information.objects.get(id=info_id)
    if str(request.user) != "alcohol_admin":
        Http404

    if request.method != "POST":
        form = InfoForm(instance=info)
    
    else:
        form = InfoForm(instance=info, data=request.POST)
        if form.is_valid:
            form.save()
        return redirect('informations:infos')

    context = {'form':form, 'info_id':info_id}
    return render(request, 'informations/edit_info.html', context=context)

def remove_and_insert(list, index):
    list.remove(index)
    list.insert(0,index)
    
