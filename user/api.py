from django.shortcuts import render
from libs.http import render_json
from user.models import Axf_User
from django.http import JsonResponse


# Create your views here.

# 用户注册
def register(request):
    u_username = request.POST.get('u_username')
    u_password = request.POST.get('u_password')
    u_email = request.POST.get('u_email')
    if u_password != request.POST.get("u_password2"):
        return render_json(data="两次密码不一致", code=1)

    user = Axf_User.objects.create(u_username=u_username, u_password=u_password, u_email=u_email)
    # 使用session记录登录状态
    # request.session['uid'] = user.id
    return render_json(data={"id": user.id})
    # return JsonResponse(data=user.to_dict(), mgs="ok", status=200)


# 用户登陆
def login():
    pass


# 用户中心
def user():
    pass
