from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth import login, authenticate
from django.conf import settings

# Create your views here.


def index(request):
    context = {}
    return render(request, '../templates/index.html', context)


def registration(request):
    context = {}
    return render(request, '../templates/registration.html', context)


def logoutpage(request):
    return render(request, '../templates/index.html')

def forgotpassword(request):
    username = request.POST.get('username')
    newpassword = request.POST.get('newpassword')
    # try to find user with matching email and change password
    try:
        user = User.objects.get(username=username)
        user.set_password(newpassword)
        user.save()
        return redirect('/')
    except User.DoesNotExist:
        user = None
    return render(request, "../templates/forgotpassword.html")


def search(request):
    context = {}
    return render(request, '../templates/search.html', context)


def productView(request):
    context = {}
    return render(request, '../templates/productView.html', context)


def cart(request):
    context = {}
    return render(request, '../templates/cart.html', context)


def checkout(request):
    context = {}
    return render(request, '../templates/checkout.html', context)


def orderConfirm(request):
    context = {}
    return render(request, '../templates/orderConfirmation.html', context)
