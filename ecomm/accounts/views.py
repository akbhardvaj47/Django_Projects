from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.models import Profile
from products.models import Product, SizeVariant, ColorVariant
from accounts.models import Cart, CartItems, Coupon
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib import messages

 # authenticate function Django ka built-in hai jo user verify karta hai
 # Agar credentials galat hain to None return hota hai, aur error message dikhakar page reload ho jata hai


'''
| Step | whats happening in register view              |
| ---- | ----------------------------------------- |
| 1    | Form data extract from html page          |
| 2    | Checks user exists in database or not     |
| 3    | Creating new user                         |
| 4    | Password securely set hota hai            |
| 5    | Send registered mail to successfully      |
| 6    | Sends Success message   '''

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=email).exists():
            messages.warning(request, "User already exists")
            return HttpResponseRedirect(request.path_info)

        user_obj = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email
        )
        user_obj.set_password(password)
        user_obj.save()

        # Send welcome email
        send_mail(f"Welcome! {first_name} {last_name}", "Thanks for registering.", "anshh9335@gmail.com", [email])

        messages.success(request, "Registration successful. An email has been sent to your email.")
        return HttpResponseRedirect(request.path_info)

    return render(request, 'accounts/register.html')




'''
| Step | What Happens                           |
| ---- | -------------------------------------- |
| 1    | Check if form is submitted (`POST`)    |
| 2    | Extract email and password             |
| 3    | Look for user with that email          |
| 4    | Authenticate the user                  |
| 5    | Handle wrong credentials               |
| 6    | Check email verification               |
| 7    | Login and redirect                     |
| 8    | Render login page if no form submitted |
'''
# user=User.objects.all().delete()
def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_obj = User.objects.filter(username=email)
        if not user_obj.exists():
            messages.warning(request, "Account not found")
            return HttpResponseRedirect(request.path_info)
       
        user = authenticate(username=email, password=password)
        
        if user is None:
            messages.warning(request, "Incorrect username or password!")
            return HttpResponseRedirect(request.path_info)

        # User model ke sath ek Profile model connected hai jisme verification ka status store hota hai.
        if not user.profile.is_email_verified:
            messages.warning(request, 'Your account is not verified')
            return HttpResponseRedirect(request.path_info)

        # Agar sab kuch sahi hai (user exists, credentials sahi hain, email verified hai), to user ko login kar deta hai.
        login(request, user)
        return redirect('/')

    return render(request, 'accounts/login.html')







def activate_account(request, email_token):
    try:
        # Retrieve the profile using the email_token
        profile = Profile.objects.get(email_token=email_token)

        # Update the email_verified status
        profile.is_email_verified = True # Sets the is_email_verified field to True to confirm that the user's email is now verified.
        profile.email_token = None  # Clears the token so that it can’t be reused.
        profile.save()

        messages.success(request, "Your account has been activated. You can now log in.")
        return redirect('/accounts/login/')  # Redirect to the login page

    except Profile.DoesNotExist:
        messages.error(request, "Invalid or expired token.")
        return redirect('/')  # Redirect to homepage if the token is invalid



from django.shortcuts import get_object_or_404

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItems, Product, SizeVariant, ColorVariant
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    size_name = request.GET.get('size')
    color_name = request.GET.get('color')
    quantity = int(request.GET.get('quantity', 1))

    # Get the selected size and color objects
    size = product.size_variant.filter(size_name=size_name).first() if size_name else None
    color = product.color_variant.filter(color_name=color_name).first() if color_name else None

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user, is_paid=False)

    # Check if the product with selected size/color already exists in the cart
    cart_item, created = CartItems.objects.get_or_create(
        cart=cart,
        product=product,
        size_variant=size,
        color_variant=color,
    )
    
    # Update the quantity of the product in the cart
    cart_item.quantity += quantity
    cart_item.save()

    return redirect('cart_view')  # Redirect to cart view after adding

from django.shortcuts import render, redirect
from .models import Cart, Coupon
from django.utils import timezone

def cart_view(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user, is_paid=False)
        cart_items = cart.cart_items.all()
        total_price = cart.get_cart_total()  # This method already calculates the total

        # Handle coupon application
        coupon_code = request.GET.get('coupon')
        discount = 0
        message = None
        if coupon_code:
            coupon = Coupon.objects.filter(code=coupon_code, expires_at__gte=timezone.now()).first()
            if coupon:
                if cart.get_cart_total() >= coupon.minimum_order:
                    discount = coupon.discount_price
                    total_price -= discount
                else:
                    message = "Your cart doesn't meet the minimum order value for this coupon."
            else:
                message = "Invalid or expired coupon code."

    else:
        cart_items = []
        total_price = 0
        message = "Please log in to view your cart."

    return render(request, 'cart/cart_view.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'coupon_code': coupon_code if coupon_code else "",
        'message': message
    })

  

def remove_cart(request, cart_item_uid):
    try:
        cart_item=CartItems.objects.get(uid=cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))  

  

def cart(request):
    # Retrieve the user's active (unpaid) cart
    cart = Cart.objects.filter(user=request.user, is_paid=False).first()
    
    # Retrieve the cart items, if any
    cart_items = cart.cart_items.all() if cart else []
    
    # Calculate the total price of all items in the cart
    cart_total = sum(item.get_product_price() for item in cart_items)
    
    # Default discount is 0
    discount = 0
    
    # Check if a valid coupon exists and apply it
    if cart and cart.coupon:
        if cart.coupon.minimum_order < cart_total:
            discount = cart.coupon.discount_price

    # Calculate the grand total after applying discount
    grand_total = cart_total - discount

    # Prepare context to pass to the template
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'cart_total': cart_total,
        'discount': discount,
        'grand_total': grand_total,  # Add the grand total here
    }

    return render(request, 'accounts/cart.html', context)



def remove_coupon(request, cart_uid):
    cart = get_object_or_404(Cart, uid=cart_uid, user=request.user)
    cart.coupon = None
    cart.save()
    messages.success(request, "Coupon removed successfully.")
    return redirect('cart')
def update_quantity(request, cart_item_uid):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItems, uid=cart_item_uid, cart__user=request.user)
        quantity = int(request.POST.get('quantity'))
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart')