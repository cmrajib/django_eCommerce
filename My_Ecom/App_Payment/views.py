from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages

from App_Order.models import Order, Cart
from App_Payment.models import BillingAddress
from App_Payment.forms import BillingForm

from django.contrib.auth.decorators import login_required
# payment
import requests
# from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
import socket
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)
    saved_address = saved_address[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request, "Shipping Address Seved!")

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].get_totals()


    return render(request, 'App_Payment/checkout.html',
                  context={'form':form,'order_items':order_items,'order_total':order_total,
                           'saved_address':saved_address})
