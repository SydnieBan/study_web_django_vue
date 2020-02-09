"""pc_study_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from course.views import MySearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('note/',include('note.urls')),
    path('course/',include('course.urls')),
    path('user_course/',include('user_course.urls')),
    url(r'^search/', include('haystack.urls')), # 全文检索框架----前后端未分离
    path('my_search/', MySearchView(), name='haystack_search'),  # 全文检索框架----前后端分离
]
