'''alcoholchecksのurlパターン'''

from django.urls import path
from . import views

app_name = 'alcoholchecks'
urlpatterns = [
    #ホームページ
    path('', views.index, name="index"),
    #記録
    path('infos/<int:user_id>/', views.infos, name="infos"),
    #記録の追加ページ
    path('new_info/<int:user_id>/', views.new_info, name="new_info"),
    #スーパーユーザーのみアクセルできる確認画面
    path('check/', views.check, name="check"),
    #記録を削除
    path('delete_info/<int:info_id>/', views.delete_info, name="delete_info"),
    #ダウンロード
    path('excel_download/', views.excel_download, name="excel_download"),
]