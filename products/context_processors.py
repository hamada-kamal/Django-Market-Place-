from products.models import  Product

def add_variable_to_context(request):
    liked_products = None
    if request.user.is_authenticated:
        customer = request.user.customer
        liked_products = Product.objects.filter(like=customer)
    return {'liked_products': liked_products,}