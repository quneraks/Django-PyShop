from django.shortcuts import render
from .models import Product
from django.templatetags.static import static


def index(request):
    return render(request, 'pages/home.html')


def products(request):
    products = Product.objects.all()
    # compute a safe image source to avoid complex template logic
    for p in products:
        if p.image_url:
            if p.image_url.startswith('http'):
                p.image_src = p.image_url
            else:
                p.image_src = static(p.image_url)
        else:
            p.image_src = ''
    return render(request, 'pages/products.html', {'products': products})

def transactions(request):
    return render(request, 'pages/transac.html')

def settings_page(request):
    return render(request, 'pages/settings.html')

def cart(request):
    return render(request, "pages/modals/cart.html")

def wishlist(request):
    return render(request, "pages/modals/wishlist.html")

def checkout(request):
    return render(request, "pages/modals/checkout.html")

def address(request):
    return render(request, "pages/modals/address.html")