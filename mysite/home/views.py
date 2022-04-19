from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    context = {}
    return render(request, '../templates/index.html', context)


def registration(request):
    context = {}
    return render(request, '../templates/registration.html', context)


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
