from django.urls import path
from . import views

app_name = 'informations'
urlpatterns = [
    #ホームページ
    path('', views.infos, name="infos"),
    #記録の追加
    path('new_info/', views.new_info, name="new_info"),
    #記録の編集
    path('edit_info/<int:info_id>/', views.edit_info, name="edit_info"),
]