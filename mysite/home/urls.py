from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration, name='registration'),
    path('productView', views.productView, name='productView'),
    path('search', views.search, name='search'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('orderConfirm', views.orderConfirm, name='orderConfirm'),
]
