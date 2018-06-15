from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from lenong_users.models import UserInfo


def index(request):
    user_id = request.session.get('user_id')
    try:
        user = UserInfo.objects.get(pk=user_id)
    except:
        user = None
    return render(request, 'index.html', {'user': user})
