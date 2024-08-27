from django.shortcuts import render, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import *
from django.db.models import Max, Min
from django.http import JsonResponse
from .cart import Cart

# Create your views here.


def index(request):
    product_list = Product.objects.all()
    lastest_product = Product.objects.order_by('date')[:3]
    top_rated = Product.objects.order_by('rating')[:3]
    category =  Category.objects.all()
    blog_posts = BlogPost.objects.all()[:3]
    review_p = ProductReview.objects.all()

    context = {
     'product_list': product_list,
     'lastest_product': lastest_product,
     'category': category,
     'blog_posts':blog_posts,
     'top_rated':top_rated,
     'review_p':review_p,
    }

    return render(request, 'index.html', context)

def shop(request):
    product_list = Product.objects.all()
    lastest_product = Product.objects.order_by('date')[:3]
    price_filter = Product.objects.aaggregate(Max("price"), Min("price"))
    category =  Category.objects.all()

    context = {
     'product_list': product_list,
     'lastest_product': lastest_product,
     'price_filter': price_filter,
     'category': category,
  
    }

    return render(request, 'shop.html', context)

def category_view(request):
  category =  Category.objects.all()
  category_count = Category.objects.count()
  context = {
    'category': category,
    'category_count': category_count,
  }
  
  return render(request, 'category_view.html', context)


def product_category(request, category_id):
  products = Product.objects.filter(category_id=category_id)
  categories = Category.objects.all()
  context = {
    'products': products,
    'categories': categories,
  }
  
  return render(request, 'product_category.html', context)

def shop_detail(request, id):
  product = Product.objects.get(id=id)
  prod_Image = ProductImage.objects.all()
  related_prod = Product.objects.filter(category=product.category)[:4]

  context = {
   'product':product,
   'prod_Image':prod_Image,
   'related_prod':related_prod
  }
  return render(request, 'shop_detail.html', context)

@login_required
def shopcart(request):
    total_cost = 0
    cart_data = request.session.get('cart_data_obj', {})

    # Calculate total prices for each item and the grand total
    for item_id, item in cart_data.items():
        price_without_dollar = item['product_price']         
        total_cost += int(item['qty']) * float(price_without_dollar) 

    return render(request, 'shopcart.html', {'cart_data': cart_data, 'total_cost': total_cost})



# def add_to_cart(request):
#     if request.method == 'GET':  # Ensure the request method is GET
#         product_id = request.GET.get('id')
#         qty = request.GET.get('qty', 1)
#         product_title = request.GET.get('product_title', '')
#         product_price = request.GET.get('product_price', '')
#         product_image = request.GET.get('product_image', '')


#         if product_id:
#             cart_product = {
#                 str(product_id): {
#                     'title': product_title,
#                     'qty': qty,
#                     'product_price': product_price,
#                     'product_image': product_image,
#                 }
#             }

#             if 'cart_data_obj' in request.session:
#                 cart_data = request.session['cart_data_obj']

#                 if str(product_id) in cart_data:
#                     cart_data[str(product_id)]['qty'] = int(qty)
#                 else:
#                     cart_data.update(cart_product)

#                 request.session['cart_data_obj'] = cart_data
#             else:
#                 request.session['cart_data_obj'] = cart_product

#             return JsonResponse({
#                 "data": request.session['cart_data_obj'],
#                 'totalcartItem': len(request.session['cart_data_obj'])
#             })
#         else:
#             return JsonResponse({'error': 'Product ID is required.'}, status=400)
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=400)


# def add_to_cart(request):
#     if request.method == 'GET':  # Ensure the request method is GET
#         product_id = request.GET.get('id')
#         qty = int(request.GET.get('qty', 1))

#         try:
#             product = Product.objects.get(id=product_id)
#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'Product not found.'}, status=404)

#         cart = Cart(request)
#         cart.add(product=product, quantity=qty)

#         total_cost = cart.get_total_price()
#         total_items = len(cart.cart)

#         return JsonResponse({
#             'totalcartItem': total_items,
#             'total_cost': total_cost,
#             'cart_items': list(cart.get_items())
#         })
#     else:
#         return JsonResponse({'error': 'Invalid request method.'}, status=400)

def add_to_cart(request):
    if request.method == 'GET':  # Ensure the request method is GET
        product_id = request.GET.get('id')
        qty = int(request.GET.get('qty', 1))
        product_title = request.GET.get('product_title', '')
        product_price = request.GET.get('product_price', '')
        product_image = request.GET.get('product_image', '')

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return JsonResponse({'error': 'Product not found.'}, status=404)

        cart = Cart(request)
        cart.add(product=product, quantity=qty)

        total_cost = cart.get_total_price()
        total_items = len(cart.cart)

        return JsonResponse({
            'totalcartItem': total_items,
            'total_cost': total_cost
        })
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)



def add_to_favorites(request):
    if request.method == 'GET':  # Ensure the request method is GET
        product_id = request.GET.get('id')

        if product_id:
            favorite_product = {
            }

            if 'favorites_data_obj' in request.session:
                favorites_data = request.session['favorites_data_obj']

                if str(product_id) not in favorites_data:
                    favorites_data.update(favorite_product)

                request.session['favorites_data_obj'] = favorites_data
            else:
                request.session['favorites_data_obj'] = favorite_product

            return JsonResponse({
                "data": request.session['favorites_data_obj'],
                'totalFavoritesItem': len(request.session['favorites_data_obj'])
            })
        else:
            return JsonResponse({'error': 'Product ID is required.'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)



def blog(request):
 blog_posts = BlogPost.objects.all()
 recent_new = BlogPost.objects.order_by('pub_date')

 context = {
   'blog_posts':blog_posts,
   'recent_new':recent_new,
 }

 return render(request, 'blog.html', context)

def blog_detail(request):

 return render(request, 'blog_detail.html')

@login_required
def checkout(request):
    cart = Cart(request)
    context = {
        'cart': cart.get_items(),  # Assuming you have this method in your cart module
        'subtotal':cart.get_subtotal(),
        'total': cart.get_total_price()
        
    }
    return render(request, 'checkout.html', context)


def contact(request):

 return render(request, 'contact.html')


# def delete_from_cart(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('id')

#         if product_id and 'cart_data_obj' in request.session:
#             cart_data = request.session['cart_data_obj']
#             if product_id in cart_data:
#                 del cart_data[product_id]
#                 request.session['cart_data_obj'] = cart_data
#                 return JsonResponse({'success': True, 'totalcartItem': len(cart_data)})
#             else:
#                 return JsonResponse({'success': False, 'error': 'Product not found in cart.'}, status=404)
#         else:
#             return JsonResponse({'success': False, 'error': 'Invalid request.'}, status=400)
#     else:
#         return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=400)
    
    
def delete_from_cart(request):
    if request.method == 'GET':
        product_id = request.GET.get('id')

        if 'cart_data_obj' in request.session:
            cart_data = request.session['cart_data_obj']

            if product_id in cart_data:
                del cart_data[product_id]

                # Update the session with the modified cart data
                request.session['cart_data_obj'] = cart_data

                # Recalculate the total cost
                total_cost = sum(
                    int(item['qty']) * float(item['product_price'])
                    for item in cart_data.values()
                )

                return JsonResponse({
                    'success': True,
                    'totalcartItem': len(cart_data),
                    'total_cost': total_cost
                })
        
        return JsonResponse({'success': False, 'error': 'Product not found in cart.'}, status=400)
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method.'}, status=400)
    

def product_search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(title__icontains=query) if query else []

    return render(request, 'product_search.html', {'products': products, 'query': query})

@login_required
def process_order(request):
    if request.method == 'POST':
        cart = Cart(request)
        subtotal = cart.get_subtotal()  # Assuming you have this method in your cart module
        total = cart.get_total_price()  # Assuming you have this method in your cart module
        
        # Check if cart exists in session
        if 'cart' in request.session:
            subtotal = cart.get_subtotal()
            total = cart.get_total_price()


        # Create a new order
        order = Order(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            country=request.POST['country'],
            address=request.POST['address'],
            address2=request.POST.get('address2', ''),
            city=request.POST['city'],
            state=request.POST['state'],
            zipcode=request.POST['zipcode'],
            phone=request.POST['phone'],
            email=request.POST['email'],
            create_account='create_account' in request.POST,
            account_password=request.POST.get('account_password', ''),
            ship_different='ship_different' in request.POST,
            order_notes=request.POST.get('order_notes', ''),
            payment_method=request.POST['payment_method'],
            total=total,
            subtotal=subtotal
        )
        order.save()

        # Add order items
        for item in cart.get_items():
            OrderItem.objects.create(
                order=order,
                product=item['product'],
                quantity=item['qty'],
                price=item['product_price'],
                total=item['total_price']
            )

        # Clear the cart
        cart.clear()

        # Return a JSON response with a SweetAlert message
        return JsonResponse({
            'success': True,
            'message': 'Thank you for your order!',
            'redirect_url': '/'
        })

    return HttpResponse("Invalid request method.", status=400)