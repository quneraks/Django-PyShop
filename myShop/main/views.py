from django.shortcuts import render
from .models import Product
from django.templatetags.static import static
from django.db.models import Q


def index(request):
    products = Product.objects.all()[:3]
    for p in products:
        if p.image_url:
            if p.image_url.startswith('http'):
                p.image_src = p.image_url
            else:
                p.image_src = static(p.image_url)
        else:
            p.image_src = ''
    return render(request, 'pages/home.html', {'products': products})


def products(request):
    q = request.GET.get('q', '').strip()
    category = request.GET.get('category', 'all')
    products = Product.objects.all()
    # filter by category first (map category keys to simple keyword matches)
    if category and category != 'all':
        cat = category.lower()
        cat_map = {
            'burgers': Q(prodname__icontains='burger') | Q(description__icontains='burger'),
            'fried_chicken': (
                Q(prodname__icontains='chicken')
                | Q(description__icontains='chicken')
                | Q(prodname__icontains='fried')
                | Q(description__icontains='fried')
                | Q(prodname__icontains='deluxe')
                | Q(description__icontains='deluxe')
                | Q(prodname__icontains='nugget')
                | Q(description__icontains='nugget')
                | Q(prodname__icontains='teriyaki')
                | Q(description__icontains='teriyaki')
            ),
            'rice_meals': Q(prodname__icontains='rice') | Q(description__icontains='rice'),
            'fries_sides': (
                Q(prodname__icontains='fries')
                | Q(description__icontains='fries')
                | Q(prodname__icontains='side')
                | Q(description__icontains='side')
                | Q(prodname__icontains='onion')
                | Q(description__icontains='onion')
                | Q(prodname__icontains='ring')
                | Q(description__icontains='ring')
                | Q(prodname__icontains='mozzarella')
                | Q(description__icontains='mozzarella')
            ),
            'pizza': Q(prodname__icontains='pizza') | Q(description__icontains='pizza'),
            'pasta': (
                Q(prodname__icontains='pasta')
                | Q(description__icontains='pasta')
                | Q(prodname__icontains='spag')
                | Q(description__icontains='spag')
                | Q(prodname__icontains='spaghetti')
                | Q(description__icontains='spaghetti')
                | Q(prodname__icontains='macaroni')
                | Q(description__icontains='macaroni')
                | Q(prodname__icontains='mac & cheese')
                | Q(description__icontains='mac & cheese')
                | Q(prodname__icontains='mac and cheese')
                | Q(description__icontains='mac and cheese')
                | Q(prodname__icontains='baked mac')
                | Q(description__icontains='baked mac')
                | Q(prodname__icontains='baked macaroni')
                | Q(description__icontains='baked macaroni')
            ),
            'drinks': (
                Q(prodname__icontains='drink')
                | Q(description__icontains='drink')
                | Q(prodname__icontains='soda')
                | Q(description__icontains='soda')
                | Q(prodname__icontains='milk tea')
                | Q(description__icontains='milk tea')
                | Q(prodname__icontains='iced tea')
                | Q(description__icontains='iced tea')
                | Q(prodname__icontains='iced coffee')
                | Q(description__icontains='iced coffee')
                | Q(prodname__icontains='coffee')
                | Q(description__icontains='coffee')
                | Q(prodname__icontains='tea')
                | Q(description__icontains='tea')
            ),
            'desserts': (
                Q(prodname__icontains='dessert')
                | Q(description__icontains='dessert')
                | Q(prodname__icontains='cake')
                | Q(description__icontains='cake')
                | Q(prodname__icontains='brownie')
                | Q(description__icontains='brownie')
                | Q(prodname__icontains='sundae')
                | Q(description__icontains='sundae')
            ),
        }
        qfilter = cat_map.get(cat)
        if qfilter is not None:
            products = products.filter(qfilter)
            if cat == 'drinks':
                teriyaki_q = Q(prodname__icontains='teriyaki') | Q(description__icontains='teriyaki')
                teriyaki_bowl_q = Q(prodname__icontains='teriyaki bowl') | Q(description__icontains='teriyaki bowl')
                products = products.exclude(teriyaki_q | teriyaki_bowl_q)
            # Ensure pizza items do not appear when another category is selected
            pizza_q = Q(prodname__icontains='pizza') | Q(description__icontains='pizza')
            if cat != 'pizza':
                products = products.exclude(pizza_q)
            # Exclude burgers when another category is selected
            burger_q = Q(prodname__icontains='burger') | Q(description__icontains='burger')
            if cat != 'burgers':
                products = products.exclude(burger_q)

    if q:
        products = products.filter(Q(prodname__icontains=q) | Q(description__icontains=q))
    # compute a safe image source to avoid complex template logic
    for p in products:
        if p.image_url:
            if p.image_url.startswith('http'):
                p.image_src = p.image_url
            else:
                p.image_src = static(p.image_url)
        else:
            p.image_src = ''
    return render(request, 'pages/products.html', {'products': products, 'q': q, 'category': category})

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