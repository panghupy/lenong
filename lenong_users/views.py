from django.shortcuts import render, redirect, reverse
from django.views.generic import View
# Create your views here.
from .models import UserInfo
from .forms import UserRegisterForm
from django.http import HttpResponse
import hashlib



# 自定义加密算法
def doPwd(password):
    sha = hashlib.sha1()
    sha.update(password.encode('utf8'))
    pwd = sha.hexdigest()
    return pwd


# 自定义登录，用来存储session
def login(request, user):
    request.session['user_id'] = user.id


# 自定义用户注销
def logout(request):
    request.session.flush()
    return redirect(reverse('goods:index'))


class UserRegister(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # 此时，user代表的是一条数据库中的记录，也就是一个用户对象，但是由于commit=False,并没有真正写入到数据库，只是创建了一个用户对象
            user.upassword = form.doPwd()
            # 此时，这条数据才被写入到数据库中
            user.save()
            return redirect(reverse('goods:index'))
        else:
            return render(request, 'register.html', {'form': form})


class UserLogin(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        uname = request.POST.get('uname')
        upassword = request.POST.get('pwd')
        try:
            user = UserInfo.objects.get(uname=uname)
        except:
            user = None
        if user:
            upassword = doPwd(upassword)
            if user.upassword == upassword:
                login(request, user)
                return redirect(reverse('goods:index'))
            else:
                return HttpResponse('密码错误')
        else:
            return HttpResponse('用户名不存在')
