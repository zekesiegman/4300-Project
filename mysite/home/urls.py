from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('logout', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('registration', views.registration, name='registration'),
    path('forgotpassword', views.forgotpassword, name='forgotpassword'),
    path('productView', views.productView, name='productView'),
    path('search', views.search, name='search'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('orderConfirm', views.orderConfirm, name='orderConfirm'),
]
