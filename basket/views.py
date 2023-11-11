from django.shortcuts import render, redirect

# Create your views here.

def view_basket(request):
    """ a view to rednder the basket contents page """
    
    return render(request, 'basket/basket.html')


def add_to_basket(request, sheetmusic_id):
    """ add sheet music to shopping basket """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if sheetmusic_id in list(basket.keys()):
        messages('you allready have this item in your basket')
    else:
        basket[sheetmusic_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])

    return redirect(redirect_url)