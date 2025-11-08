from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from myapp.models import Product




def product_list(request):
    platform = request.GET.get('platform')  # 'amazon', 'flipkart', ya None
    if platform == 'amazon':
        products = Product.objects.filter(platform='amazon')
    elif platform == 'flipkart':
        products = Product.objects.filter(platform='flipkart')
    else:
        products = Product.objects.all()  # By default: all products

    context = {'products': products}
    return render(request, 'products/product_list.html', context)
