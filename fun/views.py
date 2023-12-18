from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import logging



def index2(request):
    st = request.user.is_authenticated
    if st:
        logging.warning('用户已登录')
    else:
        logging.warning('用户未登录')
        return render(request, 'login.html')
    return render(request, 'index.html', {"username": request.user.username,"st": st})


@login_required(login_url='/login/index')
def index(request):

    return render(request, 'index.html', {"username": request.user.username})

