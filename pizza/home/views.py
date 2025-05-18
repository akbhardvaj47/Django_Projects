from django.shortcuts import render,redirect,get_object_or_404
from home.models import *
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.conf import settings
from instamojo_wrapper import instamojo

api = Instamojo(api_key=settings.API_KEY,
                auth_token=settings.AUTH_TOKEN,
                endpoint='https://www.instamojo.com/api/1.1/') 

# Create your views here.

def home(request):
    pizzas=Pizza.objects.all()
    context={'pizzas':pizzas}
    return render(request, 'home.html',context)


def register_page(request):
    if request.method=='POST':
        try:
            username=request.POST.get('name')
            password=request.POST.get('password')

            user_obj=User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/register/')
            
            user_obj=User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('/login/')
    
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
        
    return render(request, 'register.html')

def login_page(request):
    if request.method=='POST':
        try:
            username=request.POST.get('name')
            password=request.POST.get('password')

            user_obj=User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, "User not found.")
                return redirect('/login/')
            
            user_obj=authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('/')
            
            messages.error(request, "Incorrect username or password")
            return redirect('/')
    
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/login/')
    return render(request, 'login.html')



from django.contrib.auth.decorators import login_required
@login_required
def add_cart(request, pizza_uid):
    user=request.user
    pizza_obj=Pizza.objects.get(uid=pizza_uid)
    cart, _=Cart.objects.get_or_create(user=user, is_paid=False)
    cart_items=CartItems.objects.create(cart=cart, pizza=pizza_obj)

    return redirect('/')


def cart(request):
    # Get current user's unpaid cart
    cart = get_object_or_404(Cart, user=request.user, is_paid=False)

    # Get only the cart items related to this cart
    cart_items = CartItems.objects.filter(cart=cart)

    context = {
        'cart': cart,
        'cart_items': cart_items
    }
    return render(request, 'cart.html', context)


def remove_cart_items(self, cart_item_uid):
    try:
        CartItems.objects.get(uid=cart_item_uid).delete()
        return redirect('/cart/')
    except Exception as e:
        print(e)


def order(request):
    orders=Cart.objects.filter(is_paid=True, user=request.user)
    context={'orders':orders}
    return render(request, 'order.html',context)   



from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user, is_paid=False)
    cart_items = CartItems.objects.filter(cart=cart)

    if request.method == 'POST':
        try:
            response = api.payment_request_create(
                amount=cart.get_cart_total(),
                purpose="Pizza Order",
                buyer_name=request.user.username,
                email="amitkumarbhardwaj030@email.com",
                redirect_url="http://127.0.0.1:8000/success/"
            )
            # Safely extract payment_url
            if 'payment_request' in response:
                payment_url = response['payment_request']['longurl']
                return redirect(payment_url)
            else:
                messages.error(request, "Invalid payment gateway response.")
                print("Invalid Instamojo response:", response)
                return redirect('/checkout/')

        except Exception as e:
            messages.error(request, "Failed to create payment. Please try again.")
            print("Payment error:", e)
            return redirect('/checkout/')

    # Render checkout template on GET request
    context = {
        'cart': cart,
        'cart_items': cart_items
    }
    return render(request, 'checkout.html', context)
