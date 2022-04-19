from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# Create your views here.


def index(request):
    context = {}
    return render(request, '../templates/index.html', context)
