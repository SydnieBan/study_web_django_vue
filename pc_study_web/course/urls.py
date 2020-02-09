from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^get_difficulty/', views.get_difficulty, name='get_difficulty'), # 获取难度列表
    url('^get_direction/', views.get_direction, name='get_direction'), # 获取方向列表
    url('^get_classify/', views.get_classify, name='get_classify'), # 获取分类列表
    url('^get_course_by_dir/', views.get_course_by_dir, name='get_course_by_dir'), # 首页轮播图左侧课程使用视图
    url('^get_course/', views.get_course, name='get_course'), # 获取课程列表
    url('^get_course_number/', views.get_course_number, name='get_course_number'), # 获取课程列表个数
    url('^search_course/', views.search_course, name='search_course'), # 获取课程列表（搜索模糊匹配）
    url('^search_course_number/', views.search_course_number, name='search_course_number'), # 获取课程列表个数
    url('^get_course_info/', views.get_course_info, name='get_course_info'), # 获取课程详细信息
    url('^get_course_time/', views.get_course_time, name='get_course_time'), # 获取课程总时长
    url('^get_course_precourse/', views.get_course_precourse, name='get_course_precourse'), # 获取课程的前导课程
    url('^get_video_chapter/', views.get_video_chapter, name='get_video_chapter'), # 获取视频章节详细信息
    url('^get_courseware_chapter/', views.get_courseware_chapter, name='get_courseware_chapter'), # 获取课件章节详细信息
    # url('^get_chapter/', views.get_chapter, name='get_chapter'),
    url('^get_video_info/', views.get_video_info, name='get_video_info'), # 获取视频信息
    url('^get_courseware_info/', views.get_courseware_info, name='get_courseware_info'), # 获取课件信息
    url('^get_editor_info/', views.get_editor_info, name='get_editor_info'), # 代码编辑
]