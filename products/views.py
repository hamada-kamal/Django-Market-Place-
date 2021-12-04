from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .utils import *
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.decorators import login_required



def all_products(request):
    categories = Category.objects.all()
    category_slug = request.GET.get('category')
    search_qs = request.GET.get('searchname', '')
    if category_slug:
        category = Category.objects.get(CATslug=category_slug)
        products = Product.objects.filter(category=category.id)
    elif search_qs:
        products = Product.objects.filter(name__icontains=search_qs)
    else:
        products = Product.objects.all()
    data = CartData(request)
    cartItems = data['cartItems']

    return render(request, 'pages/index.html', {'products': products,'categories': categories,'cartItems': cartItems})


def product_detail(request , slug):
    product = get_object_or_404(Product ,PRDSLug=slug )
    data = CartData(request)
    cartItems = data['cartItems']
    return render(request , 'pages/details.html' , {'product' : product,'cartItems': cartItems})


def updateItem(request):
    datat = json.loads(request.body)

    productId=datat['productId']
    action =datat['action']

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
        
    elif action == 'remove':
        if orderItem.quantity>1:
            orderItem.quantity = (orderItem.quantity - 1)
    elif action == 'delete':
        orderItem.quantity = 0
    elif action == 'removeWish':
        if customer in product.like.all():
            product.like.remove(customer)     
    orderItem.save()
    if  orderItem.quantity <= 0:
        orderItem.delete()


    return JsonResponse('Item was added', safe=False)  


def cart(request):
    data = CartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    return render(request, 'pages/cart_page.html', {'items':items, 'order': order, 'cartItems': cartItems})


def checkout(request):
    data = CartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    return render(request, 'pages/checkout.html', {'items':items, 'order': order, 'cartItems': cartItems,})


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        if order.shipping == True:
            ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        )
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'].replace(",","."))
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    return JsonResponse('payment complete', safe=False)  
    

@login_required 
def likeItem(request, slug):
    customer = request.user.customer
    product = Product.objects.get(PRDSLug=slug)
    if customer in product.like.all():
        product.like.remove(customer)
    else:
        product.like.add(customer)

    return redirect(reverse('products:detail',kwargs={'slug':product.PRDSLug}))


@login_required 
def liked_product(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        liked_products = Product.objects.filter(like=customer)

    data = CartData(request)
    cartItems = data['cartItems']
    return render(request, 'pages/favorit.html', {'liked_products':liked_products, 'cartItems': cartItems,})


def autoSearch(request):
    print(request.GET)
    q_original = request.GET.get('term')
    qs = Product.objects.filter(name__icontains = q_original)
    if qs:
        print('this is',qs)
        names = []
        names+=[x.name for x in qs]
    else:
        names = ['No results']
    return JsonResponse(names, safe=False)
    
