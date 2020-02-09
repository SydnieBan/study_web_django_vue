from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$',views.index,name='index'),
    url('^get_verification_code/',views.get_verification_code,name='get_verification_code'),
    url('^insert_user/',views.insert_user,name='insert_user'),
    url('^get_user/',views.get_user,name='get_user'),
    url('^get_user_info/',views.get_user_info,name='get_user_info'),
    url('^get_user_integral/',views.get_user_integral,name='get_user_integral'),
    url('^update_user_icon/',views.update_user_icon,name='update_user_icon'),
    url('^update_user_info/',views.update_user_info,name='update_user_info'),
    url('^update_user_psw/',views.update_user_psw,name='update_user_psw'),
    url('^update_user_email/',views.update_user_email,name='update_user_email'),
    # url('^insert_integral/',views.insert_integral,name='insert_integral'),
    url('^insert_checkin/',views.insert_checkin,name='insert_checkin'),
    url('^is_checkin/',views.is_checkin,name='is_checkin'),
    url('^get_teacher/',views.get_teacher,name='get_teacher'),
    # 配置七牛云的路由，上传图片至服务器
    url('^upload_token/',views.upload_token,name='upload_token'),
]