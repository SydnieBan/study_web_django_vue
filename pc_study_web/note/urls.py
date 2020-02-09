from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^get_note/', views.get_note, name='get_note'), # 获取 note 列表
    url('^get_note_number/', views.get_note_number, name='get_note_number'),
    url('^get_note_info/', views.get_note_info, name='get_note_info'), # 获取笔记详情
    url('^update_note_info', views.update_note_info, name='update_note_info'), # 修改笔记
    url('^insert_note_info', views.insert_note_info, name='insert_note_info'), # 添加笔记
    url('^delete_note/', views.delete_note, name='delete_note'), # 删除笔记
]