'''alcoholchecksのurlパターン'''

from django.urls import path
from . import views

app_name = 'alcoholchecks'
urlpatterns = [
    #ホームページ
    path('', views.index, name="index"),
    #月ごとの記録
    path('monthes/<int:user_id>/', views.monthes, name="monthes"),
    #選択した月の記録
    path('month/<int:month_id>/', views.month, name="month"),
    #月の追加ページ
    path('new_month/<int:user_id>/', views.new_month, name="new_month"),
    #記録の追加ページ
    path('new_info/<int:month_id>/', views.new_info, name="new_info"),
    #スーパーユーザーのみアクセルできる確認画面
    path('check/', views.check, name="check"),
]