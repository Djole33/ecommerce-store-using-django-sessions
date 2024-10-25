from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order, OrderItem
from django.core.paginator import Paginator

def home(request):
    products = Product.objects.all()
    product_name = request.GET.get('product_name')
    
    if product_name:
        products = products.filter(name__icontains=product_name)

    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    return render(request, 'main/home.html', {'products': products})

def details(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'main/details.html', {'product': product})

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    product = get_object_or_404(Product, id=product_id)
    product_id = str(product.id)

    if product_id in cart:
        cart[product_id]['quantity'] += 1
    else:
        cart[product_id] = {
            'name': product.name,
            'price': str(product.price),
            'quantity': 1
        }

    request.session['cart'] = cart
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart

    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())

    return render(request, 'main/cart.html', {'cart': cart, 'total_price': total_price})

def make_order(request):
    cart = request.session.get('cart', {})

    if cart:
        order = Order.objects.create()

        for product_id, item in cart.items():
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=item['quantity']
            )

        request.session['cart'] = {}

        return render(request, 'main/order_confirmation.html', {'order': order})
    else:
        return redirect('view_cart')
    