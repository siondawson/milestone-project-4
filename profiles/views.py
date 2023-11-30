from django.shortcuts import render, get_object_or_404 
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm
from django.http import FileResponse

from checkout.models import Order
from sheet_music.models import Sheetmusic


@login_required
def profile(request):
    """display users profile"""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updates successfully')
        else:
            messages.error(request, 'Update failed, please ensure form is valid.')

    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (f'This is a past confirmation for order number {order_number}, a confirmation was sent on the order date.'))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


def download_sheetmusic(request, order_number, pdf_file):

    pdf_file = pdf_file_name
    print(pdf_file)
    downloaded_sheetmusic = pdf_file
    print(downloaded_sheetmusic)
    messages.success(request, ('Sheetmusic downloaded!'))

    context = {
        'pdf_file': pdf_file
    }

    response = FileResponse(open(downloaded_sheetmusic, 'rb'))
    
    return response

