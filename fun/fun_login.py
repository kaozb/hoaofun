import logging

from django.contrib.auth import authenticate, logout, login
from django.shortcuts import render, redirect


def funlogin(request,action):
    if action.startswith("index"):
        return render(request, 'login.html')
    if action.startswith("pass"):
        return login_mysite(request)
    if action.startswith("logout"):
        logout(request)
        return logging.error("logout"*20)
    else:
        logging.error("pass"*20)



def login_mysite(request,before="/"):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    logging.warning("登录")
    if user is not None:
        login(request, user)
        logging.warning(" 成功")
        #
        request.session.set_expiry(0)
        return redirect(before)
        # return render(request, 'index.html', {"username": request.user.username, "st": True})
    else:
        return render(request, 'login.html',{"msg":"账户或者密码有误"})


