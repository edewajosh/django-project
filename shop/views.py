from django.db import connection
from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):

    #cursor = connection.cursor()
    #cursor.execute('''SELECT * FROM Product''')
    #drugs = cursor.fetchall()
    drugs = Product.objects.raw('SELECT * FROM Product')

    category = None
    categories = Category.objects.all()
    cursor = connection.cursor()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'drugs' : drugs,
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list.html', context)

def product_list_two(request, category_slug=None):

    drugs = Category.objects.raw('SELECT * FROM shop_product')

    category = None
    categories = Category.objects.all()
    #cursor = connection.cursor()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'shop/product/list_two.html', context)

def test_comparison(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM shop_product''')
    drugs = cursor.fetchall()
    somethings = Category.objects.raw('SELECT * FROM shop_product')
    products = Product.objects.all()
    context = {
        'drugs' : drugs,
        'products' : products,
        'somethings' : somethings,
    }
    connection.close()
    return render(request, 'shop/product/query.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)
