from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket at the moment")
        return redirect(reverse('sheetmusic'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51O2YNsGdoi3no1mQT9QrwRv4LbmDFtqO2yvD6Pj8k4rSJWzTFguLtsN3EEoDdJHoAZU2hk7jlLzfl6zEf6TduPSe00isF3AY8i',
        'client_secret': 'test client',
    }

    return render(request, template, context)