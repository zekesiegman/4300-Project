from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth import login, authenticate
from django.conf import settings
from .models import Profile
from .models import Item
from .models import Cart
from .forms import RegisterForm

# Create your views here.

def index(request):
    phones = Item.objects.all()
    context = {'phones': phones}
    return render(request, '../templates/index.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    form = RegisterForm()
    return render(request, '../templates/registration.html', {'form': form})


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
        return redirect('login')
    except User.DoesNotExist:
        user = None
    return render(request, "../templates/forgotpassword.html")


def search(request):
    context = {}
    if request.method == 'POST':
        searchStr = request.POST.get('search')
        nameMatches = Item.objects.filter(name__icontains=searchStr)
        # can add more search queries and add them to matches with a |
        matches = nameMatches
        context = {'matches': matches}
        return render(request, '../templates/search.html', context)
    return render(request, '../templates/search.html', context)


def productView(request, id):
    try:
        phone = Item.objects.get(itemId=id)
        context = {"phone": phone}
        return render(request, '../templates/productView.html', context)
    except Item.DoesNotExist:
        return render(request, '../templates/index.html', context)


def cart(request):
    if request.user.is_authenticated:
        cartItemsList = Cart.objects.filter(user=request.user)
        context = {'matches': cartItemsList}
        return render(request, '../templates/cart.html', context)
    else:
        return redirect("login")


def checkout(request):
    if request.user.is_authenticated:
        cartItemsList = Cart.objects.filter(user=request.user)
        context = {'matches': cartItemsList}
        return render(request, '../templates/checkout.html', context)
    else:
        return redirect("login")


def orderConfirm(request):
    if request.user.is_authenticated:
        cartItemsList = Cart.objects.filter(user=request.user)
        context = {'matches': cartItemsList}
        return render(request, '../templates/orderConfirmation.html', context)
    else:
        return redirect("login")