from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """ a view to rednder the basket contents page """
    
    return render(request, 'basket/basket.html')
    