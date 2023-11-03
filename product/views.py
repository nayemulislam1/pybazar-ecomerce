from django.shortcuts import render, redirect
from .models import*

# Create your views here.
def product(r,id):
    cat = catagory.objects.get(id=id)
    product_all = Product.objects.filter(catagory=cat)
    return render(r, 'product/product.html', locals())


def add_to_cart(r, id):
    prod = Product.objects.get(id=id)

    
    if prod:
        cart_prod = cart.objects.filter(product=prod)
        if cart_prod:
                for i in cart_prod:
                    i.quantity += 1
                    i.save()
                    return redirect(r.META['HTTP_REFERER'])
        else:
            add_cart = cart.objects.create(user=r.user, product=prod)
            add_cart.save()
            return redirect(r.META['HTTP_REFERER'])