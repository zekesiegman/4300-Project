from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth import login, authenticate
from django.conf import settings
from .models import Profile
from .models import Item
from .models import Cart
from .forms import RegisterForm
from .forms import CheckoutForm
from django.conf import settings
from cryptography.fernet import Fernet

# Create your views here.


def index(request):
    # Gets all items from database
    phones = Item.objects.all()
    if request.user.is_authenticated:
        cartCount = Cart.objects.filter(user=request.user).count()
    else:
        cartCount= 0
    context = {'phones': phones, 'cartCount': cartCount}
    return render(request, '../templates/index.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # If values pass error checking, create user and redirect to home page
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        # Show error if form is invalid
        else:
            form = RegisterForm()
            error = True
            return render(request, '../templates/registration.html', {'form': form, 'error': error})
    form = RegisterForm()
    return render(request, '../templates/registration.html', {'form': form})


def logoutpage(request):
    return render(request, '../templates/index.html')


def forgotpassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        newpassword = request.POST.get('newpassword')
        # try to find user with matching email and change password
        try:
            user = User.objects.get(username=username)
            user.set_password(newpassword)
            user.save()
            return redirect('login')
        except User.DoesNotExist:
            error = True
            return render(request, "../templates/forgotpassword.html", {'error': error})
    return render(request, "../templates/forgotpassword.html")


def search(request):
    # If user is logged in, count cart objects
    if request.user.is_authenticated:
        cartCount = Cart.objects.filter(user=request.user).count()
    else:
        cartCount= 0
    context = {'cartCount': cartCount}
    # When user searches, get all results that match search
    if request.method == 'POST':
        searchStr = request.POST.get('search')
        nameMatches = Item.objects.filter(name__icontains=searchStr)
        # can add more search queries and add them to matches with a |
        matches = nameMatches
        context = {'matches': matches, 'cartCount': cartCount}
        return render(request, '../templates/search.html', context)
    return render(request, '../templates/search.html', context)


def productView(request, id):
    # If user is logged in, update count
    if request.user.is_authenticated:
        cartCount = Cart.objects.filter(user=request.user).count()
    else:
        cartCount= 0
    context = {'cartCount': cartCount}
    # Try to get item page, if doesn't exist, redirect to home page
    try:
        phone = Item.objects.get(itemId=id)
        context = {"phone": phone, 'cartCount': cartCount}

        # If user adds item to cart, create cart item and redirect to cart
        if request.method == "POST":
            if request.user.is_authenticated:
                cartItem = Cart.objects.create(user=request.user, item=phone, copies=1)
                return redirect("cart")
            else:
                return redirect("login")

        return render(request, '../templates/productView.html', context)
    except Item.DoesNotExist:
        return render(request, '../templates/index.html', context)


def cart(request):
    # If user is logged in
    if request.user.is_authenticated:
        cartItemsList = Cart.objects.filter(user=request.user).order_by('item_id')
        
        # Calculate final costs from cart items
        totalCost = 0
        for item in cartItemsList:
            totalCost += item.item.price
        tax = totalCost * 0.06
        finalCost = totalCost + tax

        context = {'matches': cartItemsList, 'totalCost': totalCost, 'tax': tax, 'finalCost': finalCost}
        
        # If user wants to remove a specific item from cart
        if request.method == "POST":
            removeItem = request.POST.get('item')
            removing = Cart.objects.filter(user=request.user, item=Item.objects.get(itemId=removeItem))
            
            removing[0].delete()

            return redirect('cart')

        return render(request, '../templates/cart.html', context)
    else:
        return redirect("login")

# Helper function to encrypt card info
def encrypt(cardNum):
    key = settings.ENCRYPT_KEY
    fernet = Fernet(key)
    cardEncoded =cardNum.encode()
    cardNoEncr = fernet.encrypt(cardEncoded).decode()
    return cardNoEncr

# Helper function to decrypt card info
def decrpyt(cardNum):
    key = settings.ENCRYPT_KEY
    fernet = Fernet(key)
    card_in_bites = bytes(cardNum, 'utf-8')
    decoded = fernet.decrypt(card_in_bites).decode()
    return decoded


def checkout(request):
    # If user is logged in
    if request.user.is_authenticated:
        user = request.user
        cartItemsList = Cart.objects.filter(user=user)
        context = {'matches': cartItemsList,}
        # If user submits form, create/update profile
        if request.method == 'POST':
            ccnum = request.POST.get('ccnum')
            exp = request.POST.get('exp')
            ccv = request.POST.get('ccv')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            zip = request.POST.get('zip')
            # If all entered info is valid, update database
            if ccnum is not None and exp is not None and ccv is not None and len(address) != 0 and len(city) != 0 and len(state) != 0 and zip is not None:
                cardEncrpyted = encrypt(ccnum)
                fullAddress = address + ', ' + city + ' ' + state + ', ' + zip
                # If a profile doesn't exist, create one
                if len(Profile.objects.filter(user=user)) == 0:
                    profile = Profile(user=user, cardNumber=cardEncrpyted, expiration=exp, ccv=int(ccv), billingAddress=fullAddress)
                # If a profile does exist, update all values
                else:
                    profile = Profile.objects.get(user=user)
                    profile.cardNumber = cardEncrpyted
                    profile.expiration = exp
                    profile.ccv = int(ccv)
                    profile.billingAddress = fullAddress

                profile.save()

                return redirect('orderConfirm')
            # If info is invalid, show error
            else:
                cartItemsList = Cart.objects.filter(user=user)
                error = True
                context = {'matches': cartItemsList, 'error': error}
                return render(request, '../templates/checkout.html', context)
                
        return render(request, '../templates/checkout.html', context)
    else:
        return redirect("login")


def orderConfirm(request):
    if request.user.is_authenticated:

        # Get users cart. If cart empty, redirect to cart page
        cartItemsList = Cart.objects.filter(user=request.user)
        if len(cartItemsList) == 0:
            return redirect("cart")

        # Get the user and their information
        profile = Profile.objects.get(user=request.user)
        ccEncryted = profile.cardNumber
        ccDycrypted = decrpyt(ccEncryted)

        # Calculate final costs
        totalCost = 0
        for item in cartItemsList:
            totalCost += item.item.price
        tax = totalCost * 0.06
        finalCost = totalCost + tax

        context = {'matches': cartItemsList, 'profile': profile, 'ccnum': ccDycrypted, 'total': finalCost}

        # remove items from cart here #
        for item in cartItemsList:
            item.delete()
        
        return render(request, '../templates/orderConfirmation.html', context)
    else:
        return redirect("login")