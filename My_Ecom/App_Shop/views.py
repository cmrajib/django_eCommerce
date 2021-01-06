from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from App_Shop.models import Product


class Home(ListView):
    model = Product
    template_name = 'App_shop/home.html'

class ProductDetail(DetailView):
    model = Product
    template_name = 'App_Shop/product_detail.html'