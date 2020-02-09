from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import *
# Create your views here.

def index(request):
    return HttpResponse('user...index...')



def get_verification_code(request):
    '''
    获取用户验证码
    :return:  tel
    '''
    data = json.loads(request.body)
    tel = data.get('tel')
    from utils.get_verification_code import get_verification_code
    res = get_verification_code(tel)
    return HttpResponse(json.dumps({"vc":res}))


def insert_user(request):
    '''
    添加用户
    :param request:  tel email psw register_time
    :return: 状态【Json字符串】
    '''
    from utils.password_util import password_encryption
    from utils.token_util import make_token
    data = json.loads(request.body)
    tel = data.get('tel')
    email = data.get('user_tel')
    psw = data.get('psw')
    psw_en = password_encryption(psw)
    res_json = None
    try:
        u = User.objects.create(tel=tel,email=email,psw=psw_en)
        UserInfo.objects.create(user_name='用户'+tel, user_icon_id=89,user_sex_id=1, user = u , identity='未填写',address='未填写',introduce='未填写')
        token = make_token(tel)
        res = 'insert success'
        res_json = json.dumps({"result":res,"token":token.decode(), "id": u.id})
    except Exception as ex:
        print(ex)
        res = 'insert error'
        res_json = json.dumps(json.dumps({"result":res}))
    finally:
        return HttpResponse(res_json)



def get_user(request):
    '''
    获取 User ：用户基本信息
    :param request: user_id 或 user_tel psw（登录）
    :return:  id tel   email   register_time 【Json字符串】
    '''
    from utils.password_util import password_check
    from utils.token_util import make_token
    data = json.loads(request.body)
    user_id = data.get('user_id')
    user_tel = data.get('user_tel')
    user_psw = data.get('user_psw')
    res = None
    if user_id:
        user_f = User.objects.filter(id=user_id).values('id','tel','psw','register_time','email')[0]
        res = {"id":user_f['id'],"tel":user_f['tel'],"email":user_f['email'],"register_time":user_f['register_time']}
        res['register_time'] = res['register_time'].strftime('%Y-%m-%d %H:%M:%S')
    elif user_tel:
        user_f = User.objects.filter(tel = user_tel).values('id','tel','email','psw','register_time')
        if user_f:
            user_f = user_f[0]
            judge = password_check(user_f['psw'],user_psw)
            if judge:
                token = make_token(user_tel)
                res = {"id":user_f['id'],"tel":user_f['tel'],"email":user_f['email'],"register_time":user_f['register_time'],"token":token.decode()}
                res['register_time'] = res['register_time'].strftime('%Y-%m-%d %H:%M:%S')
            else:
                res = {"result":"password error"}
        else:
            res = {"result":"user none"}
    res_json = json.dumps(res)
    return HttpResponse(res_json)



def get_user_info(request):
    '''
    获取 UserInfo ：用户信息
    :param request: user_id
    :return:  user_name  user_icon__icon_img   user_sex__name  identity  address introduce【Json字符串】
    '''
    user_id = request.GET.get('user_id')
    users = UserInfo.objects.filter(user__id = user_id).values('user_name','user_icon__icon_img','user_sex__name','identity','address','introduce')
    users_list = list(users)
    return HttpResponse(json.dumps(users_list))



def get_user_integral(request):
    '''
    获取 UserIntegral ：用户积分
    :param request: user_id
    :return: integral_sum 【Json字符串】
    '''
    from django.db.models.aggregates import Sum
    user_id = request.GET.get('user_id')
    ui = UserIntegral.objects.filter(user__id = user_id).aggregate(integral_sum = Sum('integral'))
    integral_sum = ui['integral_sum'] if ui['integral_sum'] else 0
    return HttpResponse(json.dumps({"integral_sum":integral_sum}))





def get_user_integral_by_user_id(user_id):
    '''
    获取 UserIntegral ：用户积分 ** 供其他函数调用 **
    :param : user_id
    :return: integral_sum 【int】
    '''
    from django.db.models.aggregates import Sum
    ui = UserIntegral.objects.filter(user__id = user_id).aggregate(integral_sum = Sum('integral'))
    integral_sum = ui['integral_sum'] if ui['integral_sum'] else 0
    return integral_sum




def update_user_icon(request):
    '''
    修改用户头像
    :param request: user_id  user_icon
    :return:修改状态
    '''
    user_id = request.GET.get('user_id')
    user_icon = request.GET.get('user_icon')
    icon_f = Icon.objects.filter(icon_img = user_icon).first()
    userinfo_f = UserInfo.objects.filter(user__id=user_id).first()
    res = 'update success'

    if icon_f:
        try:
            userinfo_f.user_icon = icon_f
            userinfo_f.save()
        except Exception as ex:
            print(ex)
            res = 'update error'
        finally:
            return HttpResponse(json.dumps({"result":res}))
    else:
        try:
            userinfo_f.user_icon = Icon.objects.create(icon_img=user_icon)
            userinfo_f.save()
        except Exception as ex:
            print(ex)
            res = 'update error'
        finally:
            return HttpResponse(json.dumps({"result":res}))






def update_user_info(request):
    '''
    修改用户资料
    :param request: user_id user_name  user_sex（1/3）  user_identity  user_address user_introduce【Json字符串】
    :return:修改状态
    '''
    data = json.loads(request.body)
    user_id = data.get('user_id')
    u_name = data.get('u_name')
    u_sex = data.get('u_sex')
    u_identity = data.get('u_identity')
    u_address = data.get('u_address')
    u_introduce = data.get('u_introduce')
    userinfo_f = UserInfo.objects.filter(user__id=user_id).first()
    res = None
    try:
        userinfo_f.user_name = u_name if u_name else userinfo_f.user_name
        userinfo_f.user_sex = Sex.objects.filter(id = u_sex).first() if u_sex else userinfo_f.user_sex
        userinfo_f.identity = u_identity if u_identity else userinfo_f.identity
        userinfo_f.address = u_address if u_address else userinfo_f.address
        userinfo_f.introduce = u_introduce if u_introduce else userinfo_f.introduce
        userinfo_f.save()
        res = 'update success'
    except Exception as ex:
        print(ex)
        res = 'update error'
    finally:
        return HttpResponse(json.dumps({"result":res}))




def update_user_psw(request):
    '''
    修改用户密码
    :param request: user_id / user_tel  user_psw
    :return:修改状态
    '''
    from utils.token_util import make_token
    from utils.password_util import password_encryption
    data = json.loads(request.body)
    user_id = data.get('user_id')
    user_tel = data.get('user_tel')
    user_psw = data.get('user_psw')
    user_psw = password_encryption(user_psw)
    if user_id:
        user_f = User.objects.filter(id = user_id).first()
    else:
        user_f = User.objects.filter(tel = user_tel).first()
    res_json = None
    try:
        user_f.psw = user_psw if user_psw else user_f.psw
        user_f.save()
        token = make_token(user_f.tel)
        res = 'update success'
        res_json = json.dumps({"result": res, "token": token.decode(), "id":user_f.id})
    except Exception as ex:
        print(ex)
        res_json = json.dumps({"result":"update error"})
    finally:
        return HttpResponse(res_json)




def update_user_email(request):
    '''
    修改用户邮箱
    :param request: user_id  user_email
    :return:修改状态
    '''
    data = json.loads(request.body)
    user_id = data.get('user_id')
    user_email = data.get('user_email')
    user_f = User.objects.filter(id=user_id).first()
    res_json = None
    try:
        user_f.email = user_email if user_email else user_f.email
        user_f.save()
        res = 'update success'
        res_json = json.dumps({"result": res})
    except Exception as ex:
        print(ex)
        res_json = json.dumps({"result": "update error"})
    finally:
        return HttpResponse(res_json)





def insert_integral(user_id, integral):
    '''
    添加用户积分，用于 ** 后端调用 **
    :param request: user_id  integral
    '''
    user_f = User.objects.filter(id=user_id).first()
    res = None
    try:
        UserIntegral.objects.create(integral=integral,user=user_f)
        res = 'insert success'
    except Exception as ex:
        print(ex)
        res = 'insert error'
    finally:
        return res






def insert_checkin(request):
    '''
    用户签到，并 调用insert_integral() 向 UserIntegral 加入 2 积分
    :param request: user_id
    :return: 签到状态（已签到、签到成功、签到失败）
    '''
    user_id = request.GET.get('user_id')
    user_f = User.objects.filter(id=user_id).first()
    res = None
    try:
        CheckIn.objects.create(user=user_f)
        insert_integral(user_id, 2)
        res = 'insert success'
    except Exception as ex:
        print(ex)
        res = 'insert error'
    finally:
        return HttpResponse(json.dumps({"result":res}))




def is_checkin(request):
    '''
    判断用户是否签到
    :param request: user_id
    :return: 是否签到
    '''
    # 当前时间
    import datetime
    from django.utils.timezone import utc
    utcnow = datetime.datetime.utcnow().replace(tzinfo=utc)
    # 当前时间 END
    user_id = request.GET.get('user_id')
    user_id = user_id and int(user_id)
    res = CheckIn.objects.filter(user__id=user_id,check_date__date=utcnow.date())
    if res:
        return HttpResponse(json.dumps({"result":True}))
    else:
        return HttpResponse(json.dumps({"result": False}))





def get_teacher(request):
    '''
    获取老师信息
    :param request: course_id（为空则无条件选择10个）
    :return: id name introduce  teacher_icon  teacher_sex  teacher_identity【Json字符串】
    '''
    course_id = request.GET.get('course_id')
    if course_id:
        teachers = Teacher.objects.filter(course__id=course_id).values('id','name','introduce','teacher_icon__icon_img','teacher_sex__name','teacher_identity__identity')
    else:
        teachers = Teacher.objects.filter(id__range=[3023,3032]).values('id','name','introduce','teacher_icon__icon_img','teacher_sex__name','teacher_identity__identity')[0:10]
    return HttpResponse(json.dumps(list(teachers)))







# ************************************
# 七牛云配置，返回前端token，和文件名
def upload_token(request):
    from qiniu import Auth
    import uuid
    # 1. 获取前端的filename（图片名）
    local_file_name = request.GET.get('local_file_name')
    # 2. 需要填写你的 Access Key 和 Secret Key
    access_key = 'zIBE0Qqwx4WGfUjwkPa8Mh2JGBJhI6dUpvfW8JQl'
    secret_key = 'MRR6Bla7WJy0_SKUdLKo4YoQk1uK6QUIh1VoGNTB'
    # 3. 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 4. 要上传的空间（空间名）
    # bucket_name = 'sherlockx'
    # 测试使用的空间域名
    bucket_name = 'sherlockxx'
    # 5. 上传后保存的文件名（后缀前端传过来）
    key = str(uuid.uuid4()) + '.' + local_file_name.split('.')[1]
    # 6. 生成上传 token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    # 7. 将 token、key（上传后保存到文件名）给前端即可
    return  HttpResponse(json.dumps({"upload_token": token, "new_file_name": key}))
# ************************************