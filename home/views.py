from django.shortcuts import render
from product.models import catagory, cart, User

# Create your views here.
def home(request):
    user = request.user
    all_cata = catagory.objects.all()
    if user.is_authenticated:
        cart_all = cart.objects.filter(user=request.user)[:3]
        len_cart = len(cart.objects.filter(user=request.user))
    
    # totall = 0
    # for i in cart.objects.filter(user = request.user):
    #     subtotal = i.product.new_price * i.quantity
    #     totall += subtotal
    

    return render(request, 'home/home.html', locals())