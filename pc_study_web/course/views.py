from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from utils.editor_util import main
from django.core.serializers import serialize

# Create your views here.
def index(request):
    return HttpResponse('course..index...')

def get_difficulty(request):
    '''
    获取难度列表
    :param request:(全部)
    :return:  id name 【Json字符串】
    '''
    difficulty = Difficulty.objects.all().order_by('id')
    if difficulty:
        res_list = list(difficulty.values('id', 'name'))
        return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)
    else:
        return JsonResponse({"Error": "获取数据错误"}, json_dumps_params={'ensure_ascii': False}, safe=False)



def get_direction(request):
    '''
    获取方向列表
    :param request:(全部)
    :return:  id  name 【Json字符串】
    '''
    direction = Direction.objects.all()
    if direction:
        res_list = list(direction.values('id', 'name'))
        return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)
    else:
        return JsonResponse({"Error":"获取数据错误"}, json_dumps_params={'ensure_ascii': False}, safe=False)


# 获取 Classify【这是实例。。。】
def get_classify(request):
    '''
    获取分类列表
    :param request: direction_id // direction_name（两者为空则全部查询）
    :return: id   name  direction__name
    '''
    # direction_id = None # 11
    # direction_name = '' # '后端'
    direction_id = request.GET.get('direction_id')
    direction_name = request.GET.get('direction_name')
    if direction_id:
        res = Classify.objects.filter(direction__id=direction_id).distinct()
    else:
        res = Classify.objects.filter(direction__name__icontains=direction_name).distinct()
    res_list = list(res.values('id','name','direction__name'))
    return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)

def get_course_by_dir(request):
    '''
    首页轮播图左侧课程使用视图
    :param request:  direction_name
    :return: id name course_icon difficulty__name  integral
    '''
    direction_name = request.GET.get('direction_name')
    data = Course.objects.filter(classify__direction__name__icontains=direction_name).order_by('-integral')[1:5]
    json_list = list(data.values('id','name','course_icon','difficulty__name','integral'))
    return HttpResponse(json.dumps(json_list))



def get_course(request):
    '''
    获取课程列表
    :param request: difficulty_name  direction_name  classify_name  page_index  page_items  sort_flag( 为0：按时间逆序，为1：选课人数，为2:收藏人数) integral_flag（为0：全部，为1：不免费，为2：免费）
    :return:  id  name  introduce   course_icon   integral   publish_time【Json字符串】,difficulty
    '''
    difficulty_name = request.GET.get('difficulty_name')
    direction_name = request.GET.get('direction_name')
    classify_name = request.GET.get('classify_name')
    page_index = int(request.GET.get('page_index'))  # page_index = 1
    page_items = int(request.GET.get('page_items'))  # page_items = 5
    sort_flag = int(request.GET.get('sort_flag'))   # sort_flag = 0
    integral_flag = int(request.GET.get('integral_flag'))

    if integral_flag == 1: # 不免费
        from django.db.models import Q
        data_course = Course.objects.filter(~Q(integral=0))
    elif integral_flag == 2: # 免费
        data_course = Course.objects.filter(integral=0)
    else: # 全部
        data_course = Course.objects.all()

    data_course = data_course.filter(difficulty__name__icontains=difficulty_name,classify__direction__name__icontains=direction_name,classify__name__icontains=classify_name)

    if sort_flag == 1: # 选课人数逆序
        from django.db.models import Count
        data = data_course.annotate(count=Count('selectcourse__user')).order_by('-count')[page_items * (page_index - 1): page_items * page_index]
    elif sort_flag == 2: # 收藏人数逆序
        from django.db.models import Count
        data = data_course.annotate(count=Count('collection__user')).order_by('-count')[page_items * (page_index - 1): page_items * page_index]
    else: # 时间逆序
        data = data_course.order_by('-publish_time')[page_items * (page_index - 1): page_items * page_index]

    result = data.values('id', 'name', 'introduce', 'course_icon', 'integral', 'publish_time', 'difficulty__name')
    for res in result:
        res['publish_time'] = res['publish_time'].strftime('%Y-%m-%d %H:%M:%S')
    return JsonResponse(list(result), json_dumps_params={'ensure_ascii': False}, safe=False)






def get_course_number(request):
    '''
    获取课程列表个数
    :param request: difficulty_name  direction_name  classify_name  integral_flag（为0：全部，为1：不免费，为2：免费）
    :return:  course_num 【Json字符串】
    '''
    difficulty_name = request.GET.get('difficulty_name')
    direction_name = request.GET.get('direction_name')
    classify_name = request.GET.get('classify_name')
    integral_flag = int(request.GET.get('integral_flag'))

    if integral_flag == 1: # 不免费
        from django.db.models import Q
        data_course = Course.objects.filter(~Q(integral=0))
    elif integral_flag == 2: # 免费
        data_course = Course.objects.filter(integral=0)
    else: # 全部
        data_course = Course.objects.all()

    data_course = data_course.filter(difficulty__name__icontains=difficulty_name,classify__direction__name__icontains=direction_name,classify__name__icontains=classify_name)
    data = data_course.count()
    return JsonResponse({"course_num": data}, json_dumps_params={'ensure_ascii': False}, safe=False)



def search_course(request):
    '''
    获取课程列表（搜索模糊匹配）
    :param request: search_text（即 course_name 去匹配） page_index  page_items  sort_flag( 为0：按时间逆序，为1：选课人数，为2:收藏人数)
    :return: id  name  introduce   course_icon   integral   publish_time【Json字符串】
    '''
    search_text = request.GET.get('search_text')
    page_index = int(request.GET.get('page_index'))
    page_items = int(request.GET.get('page_items'))
    sort_flag = int(request.GET.get('sort_flag'))  # sort_flag = 0


    if search_text:
        data_course = Course.objects.filter(name__icontains=search_text)

        if sort_flag == 1:  # 选课人数逆序
            from django.db.models import Count
            data = data_course.annotate(count=Count('selectcourse__user')).order_by('-count')[page_items * (page_index - 1): page_items * page_index]
        elif sort_flag == 2:  # 收藏人数逆序
            from django.db.models import Count
            data = data_course.annotate(count=Count('collection__user')).order_by('-count')[page_items * (page_index - 1): page_items * page_index]
        else:  # 时间逆序
            data = data_course.order_by('-publish_time')[page_items * (page_index - 1): page_items * page_index]

        result = list(data.values('id', 'name', 'introduce', 'course_icon', 'integral', 'publish_time', 'difficulty__name'))
        for res in result:
            res['publish_time']=res['publish_time'].strftime('%Y-%m-%d %H:%M:%S')
        return JsonResponse(result, json_dumps_params={'ensure_ascii': False}, safe=False)





def search_course_number(request):
    '''
    获取课程列表个数
    :param request: search_text（即 course_name 去匹配）
    :return:   course_num 【Json字符串】
    '''
    search_text = request.GET.get('search_text')
    if search_text:
        data = Course.objects.filter(name__icontains=search_text).count()
        return JsonResponse({"course_num": data}, json_dumps_params={'ensure_ascii': False}, safe=False)
    else:
        return JsonResponse({"Error": "请输入搜素关键词"}, json_dumps_params={'ensure_ascii': False}, safe=False)




def get_course_info(request):
    '''
    获取课程详细信息
    :param request: course_id
    :return: name  introduce   course_icon  notice  integral
    difficulty_name  direction_name
    '''

    id = request.GET.get('course_id')
    course_data = Course.objects.filter(id=id)
    # 课程名，介绍，课程图片，课程须知，
    result = list(course_data.values('name', 'introduce', 'course_icon', 'notice', 'integral', 'difficulty__name', 'classify__name', 'classify__direction__name'))
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False}, safe=False)





def get_course_time(request):
    '''
    获取课程总时长（单独一个，不直接和get_video_info（）之类的函数交互）
    :param request:  course_id
    :return: course_time【Json字符串】
    '''
    from utils.time_util import time_to_stamp,stamp_to_time
    time_stamp= 0
    course_id = request.GET.get('course_id')

    courseware_data = Courseware.objects.filter(chapter__course_id=course_id)
    courseware_time = list(courseware_data.values('courseware_time'))
    video_data = Video.objects.filter(chapter__course_id=course_id)
    video_time = list(video_data.values('video_time'))

    for i in range(len(courseware_time)):
        courseware_time[i]['courseware_time']= time_to_stamp(courseware_time[i]['courseware_time'])
        time_stamp += courseware_time[i]['courseware_time']

    for i in range(len(video_time)):
        video_time[i]['video_time'] = time_to_stamp(video_time[i]['video_time'])
        time_stamp += video_time[i]['video_time']

    course_time = stamp_to_time(time_stamp)
    return JsonResponse({"course_time":course_time}, json_dumps_params={'ensure_ascii': False}, safe=False)




def get_course_precourse(request):
    '''
    获取课程的前导课程
    :param request: course_id
    :return: id  name  difficulty__name  integral 【Json字符串】
    '''
    course_id = request.GET.get('course_id')
    course_id = course_id and int(course_id)
    pre_course_data = Course.objects.filter(id=course_id)
    pre_course_id = list(pre_course_data.values('pre_course_id', 'classify_id'))
    pre_id = pre_course_id[0]['pre_course_id']  # 228前导课程id
    classify_id = pre_course_id[0]['classify_id'] # 课程所属分类id
    if pre_id:
        pre_course = Course.objects.filter(id=pre_id)[:1]
        data = Course.objects.filter(classify_id=classify_id).order_by('-publish_time')[:5]
        res_list_for = list(pre_course.values('id', 'name', 'difficulty__name', 'integral', 'course_icon'))
        res_list_last = list(data.values('id', 'name', 'difficulty__name', 'integral','course_icon'))
        res_list = res_list_for + res_list_last
        return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)
    else:
        data = Course.objects.filter(classify_id=classify_id).order_by('-publish_time')[:6]
        res_list = list(data.values('id', 'name', 'difficulty__name', 'integral','course_icon'))
        return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)




def get_video_chapter(request):
    '''
    获取视频章节详细信息（包括哪些章哪些节）  ** 调用 get_chapter()  **
    :param request: course_id
    :return: 【Json字符串】。。。。这一部分还不确定，，
    '''
    course_id = request.GET.get('course_id')
    course_id = course_id and int(course_id)
    course_video = Video.objects.filter(chapter__course_id=course_id)
    res_list = list(course_video.values('id','name','chapter_id','video_time'))
    chapter_info = get_chapter(course_id)
    result = process_data(res_list, chapter_info, 'video_time')
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False}, safe=False)



def get_courseware_chapter(request):
    '''
    获取课件章节详细信息（包括哪些章哪些节）  ** 调用 get_chapter() **
    :param request: course_id
    :return: 【Json字符串】。。。。这一部分还不确定，，
    '''
    course_id = request.GET.get('course_id')
    course_id = course_id and int(course_id)
    course_courseware = Courseware.objects.filter(chapter__course_id=course_id)
    res_list = list(course_courseware.values('id', 'name', 'chapter_id', 'courseware_time'))
    chapter_info = get_chapter(course_id)
    result = process_data(res_list, chapter_info, 'courseware_time')
    return JsonResponse(result, json_dumps_params={'ensure_ascii': False}, safe=False)


def process_data(res_list, chapter_info, type):
    '''
      处理数据，把课程视频的章节合并为一个字典列表
      :param request: res_list(小章节内容)，chapter_inf(每章节大标题)，name(新建键名)
      :return: [{"id":, "name":"", "introduce":"", "sections":[ {"section_name":"", "section_id": "", "section_time":"" },{}] },{}]
      '''
    for i in range(len(chapter_info)):
        chapter_info[i]['sections'] = None
        for j in range(len(res_list)):
            if chapter_info[i]['id'] == res_list[j]['chapter_id']:
                if chapter_info[i]['sections']:
                    chapter_info[i]['sections'].append({"section_name": res_list[j]['name'], "section_id": res_list[j]['id'], "section_time":res_list[j][type]})
                else:
                    chapter_info[i]['sections'] = [{"section_name": res_list[j]['name'], "section_id": res_list[j]['id'], "section_time":res_list[j][type]}]
    return chapter_info


def get_chapter(course_id):
    '''
    获取课程章信息
    :param request: course_id
    :return: id  name  introduce【Json字符串】
    '''
    chapter_data = Chapter.objects.filter(course__id=course_id)
    res_list = list(chapter_data.values('id','name','introduce'))
    return res_list





# def get_video(request):
#     '''
#     获取视频列表
#     :param request: chapter_id
#     :return: id name video_time【Json字符串】
#     '''
#     pass


# def get_courseware(request):
#     '''
#     获取课件列表
#     :param request:  chapter_id
#     :return: id name courseware_time 【Json字符串】
#     '''
#     pass




def get_video_info(request):
    '''
    获取视频信息
    :param request: video_id
    :return: id  name  video_src  video_time  chapter_id 【Json字符串】
    '''
    video_id = request.GET.get('video_id')
    video_data = Video.objects.filter(id=video_id)
    res_list = list(video_data.values('id', 'name', 'video_src', 'video_time', 'chapter_id'))
    return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)




def get_courseware_info(request):
    '''
    获取课件信息
    :param request: courseware_id
    :return: id name content  courseware_time chapter_id【Json字符串】
    '''
    courseware_id = request.GET.get('courseware_id')
    courseware_data = Courseware.objects.filter(id=courseware_id)
    res_list = list(courseware_data.values('id', 'name', 'content', 'courseware_time', 'chapter_id'))
    return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)


def get_editor_info(request):
    '''
    代码编辑
    :param request:
    :return:
    '''
    from utils.editor_util import main
    code = json.loads(request.body)
    res = main(code['code'])
    return JsonResponse(res,json_dumps_params={'ensure_ascii': False}, safe=False )





# 要想实现搜索接口的编写,必须重写SearchView
from haystack.views import SearchView
class MySearchView(SearchView):

    def create_response(self):#重载create_response来实现接口编写
        context = super().get_context()#搜索引擎完成后的内容
        # http://localhost:8080/my_search/?q=html&page=4
        keyword = self.request.GET.get('q', None)#关键子为q
        # now_page = 1
        if not keyword:
            return JsonResponse({"status": {"code": 400, "msg": {"error_code": 4450, "error_msg": "关键字错误"}}})
        # content = {"status": {"code": 200, "msg": "ok"}, "data": {"page": now_page, "next_page": now_page+1, "sort": '默认排序', }}
        content = {"status": {"code": 200, "msg": "ok"}}
        content_list = []
        page_num = int(str(context['page']).strip('<>').split('of')[1]) # 一共多少页
        for i in context['page'].object_list:#对象列表

            intro = i.object.introduce
            intro_i = intro.find(keyword)
            if intro_i>0:
                intro = '...'+intro[intro_i:]
            set_dict = {
                'id': i.object.id, 'name': i.object.name, 'introduce': intro,
                'course_icon': i.object.course_icon,'integral': i.object.integral,
                'publish_time': i.object.publish_time.strftime('%Y-%m-%d %H:%M:%S'),
                'classify__name': i.object.classify.name, 'difficulty__name': i.object.difficulty.name,
                'classify__direction__name': i.object.classify.direction.name
            }#要返回的字段
            content_list.append(set_dict)
        content["data"]=dict({"course_num":page_num*30, "data":content_list})
        return HttpResponse(json.dumps(content,ensure_ascii=False))#对对象进行序列化返回json格式数据

