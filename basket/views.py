from django.shortcuts import (
    render, redirect, HttpResponse, get_object_or_404)
from django.contrib import messages

from sheet_music.models import Sheetmusic


def view_basket(request):
    """ a view to rednder the basket contents page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, sheetmusic_id):
    """ add sheet music to shopping basket """

    sheetmusic = Sheetmusic.objects.get(pk=sheetmusic_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if sheetmusic_id in list(basket.keys()):
        basket[sheetmusic_id] += quantity
    else:
        basket[sheetmusic_id] = quantity
        messages.success(request, f'Added {sheetmusic.name} to your basket')

    request.session['basket'] = basket

    return redirect(redirect_url)


def remove_from_basket(request, sheetmusic_id):
    """ Remove item from basket """
    try:

        sheet_music = get_object_or_404(Sheetmusic, pk=sheetmusic_id)
        basket = request.session.get('basket', {})
        basket.pop(sheetmusic_id)
        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
