from django.shortcuts import (
    render, redirect, HttpResponse, get_object_or_404)
from django.contrib import messages

from sheet_music.models import Sheetmusic


def view_basket(request):
    """ a view to rednder the basket contents page """
    
    return render(request, 'basket/basket.html')


def add_to_basket(request, sheetmusic_id):
    """ add sheet music to shopping basket """

    quantity = int(request.POST.get('quantity'))
    print(quantity)
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if sheetmusic_id in list(basket.keys()):
        basket[sheetmusic_id] += quantity
    else:
        basket[sheetmusic_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])

    return redirect(redirect_url)


def remove_from_basket(request, sheetmusic_id):
    """ Remove item from basket """
    try:   

        sheet_music = get_object_or_404(Sheetmusic, pk=sheetmusic_id)
        print(sheet_music)
        basket = request.session.get('basket', {})
        print(basket)
        basket.pop(sheetmusic_id)


        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)