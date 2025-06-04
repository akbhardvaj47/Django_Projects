from django.shortcuts import render
from products.models import Product, Category

def index(request):
    products=Product.objects.all()
    return render(request, 'home/index.html',{'products':products})

from django.db.models import Q
def search(request):
    keyword = request.GET.get('keyword', '')
    products = Product.objects.none()
    if keyword:
        products = Product.objects.filter(Q(product_name__icontains=keyword)| Q(product_desc__icontains=keyword))
    
    context = {
        'keyword': keyword,
        'products': products,
    }    
    return render(request, 'search.html', context)