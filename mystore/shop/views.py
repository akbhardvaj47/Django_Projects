from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    data={}
    products = Product.objects.all()
    nSlides = ceil(len(products) / 4)
    slides = [products[i:i + 4] for i in range(0, len(products), 4)]
   # products = Product.objects.all()  # Product model ke saare records (products) ko database se fetch karta hai.
    #n = len(products) # Count Total number of products
    #nSlides = ceil(n / 4)  # Har slide mein 4 products dikh rahe hain, to total kitni slides banengi ye calculate karta hai.
    #slides = [products[i:i + 4] for i in range(0, n, 4)] # Ye line products ko groups of 4 mein divide karti hai.

    '''
    E.g., agar 10 products hain:
slides = [
    [product1, product2, product3, product4],
    [product5, product6, product7, product8],
    [product9, product10]
]
'''
    data={
        'slides': slides,
        'range': range(nSlides)
    }
    return render(request, 'shop/index.html',data)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse('This is contact page')

def tracker(request):
    return HttpResponse('This is tracker page')

def productView(request):
    return HttpResponse('This is product page')

def search(request):
    return HttpResponse('This is search page')

def checkout(request):
    return HttpResponse('This is checkout page')
