from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from .models import Month, Info
from .forms import MonthForm, InfoForm
import datetime
from re import sub
import io
import xlsxwriter
import openpyxl as xl
from openpyxl.writer.excel import save_virtual_workbook
from openpyxl.styles.borders import Border, Side
from openpyxl.styles import Font
from openpyxl.styles import Alignment

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
    download = ""
    check = ""
    if request.user != user and str(request.user) != "alcohol_admin":
        raise Http404
    if str(request.user) == "alcohol_admin":
        delete = "削除"
        download = "ダウンロード"
        check = "チェックする"
    monthes = user.month_set.all()
    context = {'monthes':monthes, 'user':user, 'delete':delete, 'download':download, 'check':check}
    return render(request, 'alcoholchecks/monthes.html', context)

@login_required
def month(request, month_id):
    month = Month.objects.get(id=month_id)
    delete = ""
    if month.owner != request.user and str(request.user) != "alcohol_admin":
        raise Http404
    if str(request.user) == "alcohol_admin":
        delete = "削除"
        check = "チェックする"
    infos = month.info_set.order_by('-date_added')
    context = {'month':month, 'infos':infos, 'delete':delete, 'check':check}
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
def excel_download(request, month_id):
    month = Month.objects.get(id=month_id)
    mon = sub(r"\D", "", month.month)
    user = month.owner
    output = io.BytesIO()
    book = xlsxwriter.Workbook(output)
    ws = book.add_worksheet('test')
    filename = "{}_{}_data.xlsx".format(str(user), mon)
    header = ["日時", "車両ナンバー", "アルコール検知", "確認者"]
    for i, j in enumerate(header):
        ws.write(3, i, j)
    infos = month.info_set.all()
    for index,info in enumerate(infos):
        info.date_added += datetime.timedelta(hours=9)
        ws.write(index+4, 0, info.date_added.strftime('%Y/%m/%d %H:%M'))
        ws.write(index+4, 1, int(info.carnumber))
        ws.write(index+4, 2, info.alcohol)
        ws.write(index+4, 3, "武村義治")
    book.close()
    output.seek(0)
    wb = xl.load_workbook(output)
    sheet = wb.worksheets[0]
    sheet.title = f"{mon}月"
    #罫線
    side = Side(style='thin', color='000000')
    border = Border(top=side, bottom=side, left=side, right=side)

    #フォントを設定する
    font = Font(name='メイリオ')

    #書式設定
    alignment = Alignment(horizontal='center', vertical='center')

    #columnの数繰り返す
    for col in sheet.columns:
        max_length = 0#一番文字数が多い文字列の文字数
        column = col[0].column_letter

        for cell in col:#一番文字数が多い文字の文字数をmax_lengthにいれる
            if len(str(cell.value)) > max_length:#文字数よりmax_lengthが多かったらmax_lengthを更新
                max_length = len(str(cell.value))
            cell.font = font #フォント
            cell.border = border #罫線を引く
            cell.alignment = alignment #中央に寄せる
    
        sheet.column_dimensions[column].width = (max_length+2) *2
    sheet.merge_cells('A1:D3')
    sheet.cell(1, 1).value = f"{str(user)} {mon}月"
    sheet.cell(1, 1).font = xl.styles.fonts.Font(size=35)
    wb.save(output)
    response = HttpResponse(content=save_virtual_workbook(wb))
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

