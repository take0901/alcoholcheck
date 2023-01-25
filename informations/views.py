from django.shortcuts import render, redirect
from .models import Information
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .forms import InfoForm

@login_required
def infos(request):
    infos = Information.objects.all().order_by('-year', "-month")
    year_list = sorted(list(Information.objects.values_list("year", flat=True).distinct()))
    month_list = sorted(list(Information.objects.values_list("month", flat=True).distinct()))
    motouke_list = list(Information.objects.values_list("motouke", flat=True).distinct())
    year_list.insert(0,"すべての")
    month_list.insert(0,"すべての")
    motouke_list.insert(0,"すべて")
    if request.method == "POST" and request.POST.get("reset") != "reset":
        years, months, motoukes = [],[],[] 
        year = request.POST['year']
        if year == "すべての":
            years = sorted(list(Information.objects.values_list("year", flat=True).distinct()))
        else:
            years.append(int(year))
            remove_and_insert(year_list, int(year))
        month = request.POST['month']
        if month == "すべての":
            months = sorted(list(Information.objects.values_list("month", flat=True).distinct()))
        else:
            months.append(int(month))
            remove_and_insert(month_list, int(month))
        motouke = request.POST['motouke']
        motoukes.append(motouke)
        if motouke == "すべて": 
            motoukes = list(Information.objects.values_list("motouke", flat=True).distinct())
        else:
            remove_and_insert(motouke_list, motouke)
        print(years)
        infos = Information.objects.filter(year__in=years, month__in=months
        ,motouke__in=motoukes).order_by("-year", '-month')
    context = {'infos':infos, 'years':year_list, 'months':month_list, 'motoukes':motouke_list}
    return render(request, 'informations/infos.html', context)

@login_required
def new_info(request):
    years = sorted(list(Information.objects.values_list("year", flat=True).distinct()))
    months = sorted(list(Information.objects.values_list('month', flat=True).distinct()))
    companies = Information.objects.values_list("motouke", flat=True).distinct()
    kouzis = Information.objects.values_list('kouzi', flat=True).distinct()
    places = Information.objects.values_list("place", flat=True).distinct()
    
    if request.method != 'POST':
        #フォームを生成
        form = InfoForm()
    else:
        #POSTで送信されたデータを処理
        form = InfoForm(data=request.POST)
        if form.is_valid():
            new_info = form.save(commit=False)
            new_info.year = request.POST.get('y')
            new_info.month = request.POST.get('m')
            new_info.motouke = request.POST.get('c')
            new_info.kouzi = request.POST.get('k')
            new_info.place = request.POST.get('p')
            new_info.save() 
            return redirect('informations:infos')
    context = {'form':form, 'years':years, 'months':months,
     'companies':companies, 'kouzis':kouzis, 'places':places}
    return render(request, 'informations/new_info.html', context)

@login_required
def edit_info(request, info_id):
    years = sorted(list(Information.objects.values_list("year", flat=True).distinct()))
    months = sorted(list(Information.objects.values_list('month', flat=True).distinct()))
    companies = Information.objects.values_list("motouke", flat=True).distinct()
    kouzis = Information.objects.values_list('kouzi', flat=True).distinct()
    places = Information.objects.values_list("place", flat=True).distinct()
    info = Information.objects.get(id=info_id)
    if str(request.user) != "alcohol_admin":
        Http404

    if request.method != "POST":
        form = InfoForm(instance=info)
    
    else:
        form = InfoForm(instance=info, data=request.POST)
        if form.is_valid:
            edit_info = form.save(commit=False)
            edit_info.year = int(request.POST['y'])
            edit_info.month = int(request.POST['m'])
            edit_info.motouke = request.POST['c']
            edit_info.kouzi = request.POST['k']
            edit_info.place = request.POST['p']
            edit_info.save()
        return redirect('informations:infos')

    context = {'form':form, 'info_id':info_id, 'info':info, 'years':years, 'months':months, 
                'companies':companies, 'kouzis':kouzis, 'places':places}
    return render(request, 'informations/edit_info.html', context=context)

def remove_and_insert(list, index):
    list.remove(index)
    list.insert(0,index)
    
