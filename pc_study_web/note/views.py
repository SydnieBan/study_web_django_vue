from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import json

# Create your views here.
def index(request):
    return HttpResponse('note...index...')


def get_note(request):
    '''
    获取 note
    :param request:  user_id  note_page_index  note_page_items
    :return: id   title   content_editor   publish_date   classify   mold 【Json字符串】
    '''
    user_id = request.GET.get('user_id')
    note_page_index = int(request.GET.get('note_page_index'))
    note_page_items = int(request.GET.get('note_page_items'))
    note_data = Note.objects.filter(user_id=user_id).order_by('-publish_date')[note_page_items * (note_page_index - 1): note_page_items * note_page_index]
    res_list = list(note_data.values('id', 'title', 'content_editor', 'publish_date', 'classify', 'mold'))
    for res in res_list:
        res['publish_date'] = res['publish_date'].strftime('%Y-%m-%d %H:%M:%S')
    return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)


def get_note_number(request):
    '''
    获取 笔记个数
    :param request: user_id
    :return: note_num 【Json字符串】
    '''
    user_id = request.GET.get('user_id')
    note_num = Note.objects.filter(user_id=user_id).count()
    return JsonResponse({"note_num":note_num}, json_dumps_params={'ensure_ascii': False}, safe=False)




def get_note_info(request):
    '''
    获取笔记详情
    :param request:  note_id
    :return: title  content_html  content_editor  publish_date classify  mold 【Json字符串】
    '''
    note_id = request.GET.get('note_id')
    note_data = Note.objects.filter(id=note_id)
    res_list = list(note_data.values('title', 'content_html', 'content_editor', 'publish_date', 'classify', 'mold'))
    for res in res_list:
        res['publish_date'] = res['publish_date'].strftime('%Y-%m-%d %H:%M:%S')
    return JsonResponse(res_list, json_dumps_params={'ensure_ascii': False}, safe=False)

def update_note_info(request):
    '''
    修改笔记
    :param request: {note_id,content_html,content_editor,classify,mold}
    :return:
    '''
    note_data = json.loads(request.body)
    try:
        note_state = Note.objects.filter(id=note_data['note_id'])\
            .update(content_editor=note_data['content_editor'],content_html=note_data['content_html'])
        if note_state:
            state = {"success": "修改成功"}
        else:
            state = {"error": "更新失败"}
        return JsonResponse(state, json_dumps_params={'ensure_ascii': False}, safe=False)
    except Exception as e:
        print(e)
    return HttpResponse('ok')

def insert_note_info(request):
    '''
    添加笔记
    :param request: user_id
    :return:
    '''
    note_data = json.loads(request.body)
    try:
        data = Note.objects.create(**note_data)
        data.save()
        if data:
            state = {"success": "添加笔记成功"}
        else:
            state = {"error": "添加笔记失败"}
        return JsonResponse(state, json_dumps_params={'ensure_ascii': False}, safe=False)
    except Exception as e:
        print(e)
    return HttpResponse('ok')

def delete_note(request):
    '''
    删除笔记
    :param request: note_id
    :return:
    '''
    note_id = request.GET.get('note_id')
    try:
        note_data = Note.objects.filter(id=note_id).delete()
        if note_data:
            state = {"success": "删除笔记成功"}
        else:
            state = {"error": "删除笔记失败"}
        return JsonResponse(state, json_dumps_params={'ensure_ascii': False}, safe=False)
    except Exception as e:
        print(e)
    return HttpResponse('ok')


