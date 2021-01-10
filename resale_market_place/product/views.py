from django.shortcuts import render
from .models import Product, Category
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import get_object_or_404
# Create your views here.


def productlist(request , category_slug=None):
    category = None
    products = Product.objects.all()
    allproducts = products
    # categorylist = Category.objects.annotate(total_products=Count('product'))
    categorylist = Category.objects.all()

    if category_slug :
        category = get_object_or_404(Category ,slug=category_slug)
        products = products.filter(category=category)

    search_query = request.GET.get('q')
    if search_query :
        products = products.filter(
            Q(name__icontains = search_query) |
            Q(description__icontains = search_query)|
            Q(condition__icontains = search_query)|
            Q(brand__brand_name__icontains = search_query) |
            Q(category__category_name__icontains = search_query)
        )

    paginator = Paginator(products, 1) # Show 25 contacts per page
    page = request.GET.get('page')
    products = paginator.get_page(page)

    template = 'Product/product_list.html'

    context = {
        'allproducts': allproducts,
        'product_list' : products ,
        'category_list' : categorylist ,
        'category' : category
    }

    return render(request , template , context)




def productdetail(request , product_slug):
    # print(product_slug)
    product = Product.objects.get(slug=product_slug)

    template = 'Product/product_detail.html'
    context = {
        'product_detail' : product ,
    }
    return render(request , template , context)