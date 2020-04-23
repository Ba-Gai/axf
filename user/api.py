from django.shortcuts import render
from libs.http import render_json
from user.models import Axf_User

# Create your views here.

# 用户注册
def register(request):
    u_username = request.POST.get('u_username')
    u_password = request.POST.get('u_password')
    u_email = request.POST.get('u_email')
    if u_password != request.POST.get("u_password2"):
        return render_json(msg="两次密码不一致", code=1)

    user = Axf_User.objects.create(u_username=u_username, u_password=u_password, u_email=u_email)
    return render_json(data=user.to_dict())
    # return JsonResponse(data=user.to_dict(), mgs="ok", status=200)


# 用户登陆
def login(request):
    u_username = request.POST.get('u_username')
    u_password = request.POST.get('u_password')
    user = Axf_User.objects.get(u_username=u_username, u_password=u_password)
    # 使用session记录登录状态
    request.session['uid'] = user.id
    return render_json(data=user.to_dict())


# 用户中心
def user():
    pass
