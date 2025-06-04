from django.shortcuts import render, get_object_or_404
from .models import Product

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    
    # Get the selected size and color from the query parameters
    selected_size = request.GET.get('size')
    selected_color = request.GET.get('color')

    # Get the updated price based on the selected size and color
    updated_price = product.get_updated_price(selected_size, selected_color)

    # Pass the selected size, color, and updated price to the template
    context = {
        'product': product,
        'selected_size': selected_size,
        'selected_color': selected_color,
        'updated_price': updated_price,
    }

    return render(request, 'product/product.html', context)
