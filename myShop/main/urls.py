from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('products/', views.products, name='products'),
    path('transactions/', views.transactions, name='transactions'),
    path('settings/', views.settings_page, name='settings'),

    path("cart/", views.cart, name="cart"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("checkout/", views.checkout, name="checkout"),
    path("address/", views.address, name="address"),
    path("confirmation/", views.confirmation, name="confirmation"),
]