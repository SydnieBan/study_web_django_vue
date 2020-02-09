from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url('^is_collection/',views.is_collection,name='is_collection'), # 判断是否收藏
    url('^collection_course/',views.collection_course,name='collection_course'), # 收藏课程
    url('^delete_collection_course/',views.delete_collection_course,name='delete_collection_course'), # 取消收藏
    url('^get_collection_number/',views.get_collection_number,name='get_collection_number'), # 获取收藏人数

    url('^get_collection_peruser/',views.get_collection_peruser,name='get_collection_peruser'), # 查询用户收藏的所有课程
    url('^get_collection_number_peruser/',views.get_collection_number_peruser,name='get_collection_number_peruser'),

    url('^is_sc/',views.is_sc,name='is_sc'), # 判断用户是否选课
    url('^insert_sc/',views.insert_sc,name='insert_sc'), # 添加用户选课
    # url('^update_sc/',views.update_sc,name='update_sc'),
    url('^get_sc_number/',views.get_sc_number,name='get_sc_number'), # 查询选课人数

    url('^get_sc_peruser/',views.get_sc_peruser,name='get_sc_peruser'), # 查询某用户选择的课程
    url('^get_sc_number_peruser/',views.get_sc_number_peruser,name='get_sc_number_peruser'),

    url('^study_progress/',views.study_progress,name='study_progress'), # 获取用户学习进度
    url('^study_time/',views.study_time,name='study_time'), # 获取用户学习时间
    url('^insert_course_eva/',views.insert_course_eva,name='insert_course_eva'), # 添加用户对课程的评价
    url('^get_course_eva/',views.get_course_eva,name='get_course_eva'), # 查询该课程的所有用户评价
    url('^get_course_eva_number/',views.get_course_eva_number,name='get_course_eva_number'), # 查询该课程的所有用户评价个数

    url('^insert_user_video/',views.insert_user_video,name='insert_user_video'), # 添加用户看视频的进度
    url('^update_user_video/',views.update_user_video,name='update_user_video'), # 修改用户看视频的进度
    url('^get_user_video/',views.get_user_video,name='get_user_video'), # 查询用户看视频的进度
    url('^insert_question_video/',views.insert_question_video,name='insert_question_video'), # 添加用户对某视频的提问
    url('^get_question_video/',views.get_question_video,name='get_question_video'), # 查询某视频的所有用户提问
    url('^get_question_number_video/',views.get_question_number_video,name='get_question_number_video'), # 查询某视频的所有用户提问个数

    url('^insert_user_courseware/',views.insert_user_courseware,name='insert_user_courseware'), # 添加用户课件
    url('^get_user_courseware/',views.get_user_courseware,name='get_user_courseware'),
    url('^insert_question_courseware/',views.insert_question_courseware,name='insert_question_courseware'), # 添加用户对某课件的提问
    url('^get_question_courseware/',views.get_question_courseware,name='get_question_courseware'), # 查询某课件的所有用户提问
    url('^get_question_number_courseware/',views.get_question_number_courseware,name='get_question_number_courseware'), # 查询某课件的所有用户提问个数
]