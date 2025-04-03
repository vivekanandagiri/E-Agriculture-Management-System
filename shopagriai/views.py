import http
import json
from django.shortcuts import render,get_object_or_404,redirect
from multiprocessing import context
from .models import Category
from .models import Product,Order,OrderItem,Customer,ShippingAddress
from collections import defaultdict
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
import datetime
from django.contrib.auth.decorators import login_required

# Category
@login_required(login_url='/authlogin/')
def category(request):
    categories = Category.objects.all()  # Assuming Category is your model name
    products = Product.objects.all()
    category_counts = defaultdict(int)
    #for product in products:
        #category_counts[product.category]+=1
    #category_counts = {category.id: category.products.count() for category in categories}
    for product in products: 
        category_counts[product.category.id] += 1
    context = {
        'category': categories,
        'category_counts': dict(category_counts),
    }
    print(category_counts)
    return render(request, 'category.html', context)

#Shop
#@login_required(login_url='/authlogin/')
def shop(request):
    if request.user.is_authenticated:
        try:
            customer = request.user.customer
        except Customer.DoesNotExist:
            customer = Customer.objects.create(user=request.user)

        #customer = request.user.customer
        orders = Order.objects.filter(customer=customer, complete=False)
        
        if orders.exists():
            # Take the first incomplete order or handle duplicates if necessary
            order = orders.first()
        else:
            order = Order.objects.create(customer=customer, complete=False)
        
        items = order.orderitem_set.all()
        cartItems=order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,'shipping:':False}
        cartItems=order['get_cart_items']
    
    products = Product.objects.all().order_by('id')  # Assuming Product is your model name
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': page_obj,  # Pass the page object to the template
        'cartItems':cartItems,
    }
    return render(request, 'shop.html', context)

#Category view
@login_required(login_url='/authlogin/')
def category_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 10)  # Show 10 products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'products': page_obj,
    }
    return render(request, 'category_view.html', context)



def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=id)[:6] # Adjust as needed
    context = {
        'product': product,
        'related_products':related_products,
    }
    return render(request, 'detailproduct.html', context)


#Cart View
@login_required(login_url='/authlogin/')
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer, complete=False)
        
        if orders.exists():
            # Take the first incomplete order or handle duplicates if necessary
            order = orders.first()
        else:
            order = Order.objects.create(customer=customer, complete=False)
        
        items = order.orderitem_set.all()
        count_item=len(items)
        #print(count_item) Debuging
        #cartItems=order['get_cart_items']
        
        cartItems = sum(item.quantity for item in items)
        for item in items: 
            item.total_price = item.product.price * item.quantity
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,'shipping:':False}
        count_item = order['get_cart_items']
        cartItems=order['get_cart_items']
    
    context = {'items': items, 'order': order, 
               'count_item':count_item,
               'cartItems':cartItems}
    return render(request, 'cart.html', context)
#Checkout
@login_required(login_url='/authlogin/')
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer, complete=False)
        
        if orders.exists():
            # Take the first incomplete order or handle duplicates if necessary
            order = orders.first()
        else:
            order = Order.objects.create(customer=customer, complete=False)
        
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0,'shipping:':False}
        cartItems = order['get_cart_items']
    print(items)## debugging
    context = {'items': items, 'order': order,'cartItems':cartItems}
    return render(request, 'checkout.html',context)
# Add tocart 

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    orders = Order.objects.filter(customer=customer, complete=False)
    
    if orders.exists():
        # Take the first incomplete order or handle duplicates if necessary
        order = orders.first()
        print(order)
    else:
        order = Order.objects.create(customer=customer, complete=False)
        print(order)
    #order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    print(orderItem,created)
    
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
                
    return JsonResponse('Item was added', safe=False)
##Process Order
def processOrder(request):
    
    print('Data:',request.body)
    transaction_id=datetime.datetime.now().timestamp()
    data=json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer, complete=False)
        
        if orders.exists():
            # Take the first incomplete order or handle duplicates if necessary
            order = orders.first()
        else:
            order = Order.objects.create(customer=customer, complete=False)
        total=float(data['form']['total'])
        order.transaction_id=transaction_id
        if total==order.get_cart_total:
            order.complete=True
        order.save()
        if order.shipping == True:
            ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['pincode'],
            )
        return JsonResponse({'success': True, 'transaction_id': order.transaction_id}, safe=False)

    else:
        print('User is not Logged in... ')
    return JsonResponse('Payment Submitted..',safe=False)

def order_success(request, transaction_id):
    print(f"Transaction ID: {transaction_id}")
    order = get_object_or_404(Order, transaction_id=transaction_id)
    print(f"Order: {order}")
    return render(request, 'order_success.html', {'order': order})

def user_orders(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        orders = Order.objects.filter(customer=customer).order_by('-date_ordered')
        return render(request, 'user_orders.html', {'orders': orders})
    else:
        return redirect('shop')  # Redirect to login page if not authenticated

from .forms import ProductSearchForm

def search_products(request):
    form = ProductSearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = ProductSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Product.objects.filter(name__icontains=query)

    return render(request, 'search_results.html', {'form': form, 'query': query, 'results': results})

