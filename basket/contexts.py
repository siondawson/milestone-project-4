from decimal import Decimal
from django.conf import settings 

def basket_contents(request):  # context processor to make bag contents available ot whole application

    basket_items = []
    total = 0
    basket_count = 0
    grand_total = 0

    context = {
        'basket_items': basket_items,
        'total': total,
        'basket_count': basket_count,
        'grand_total': grand_total,
    }

    grand_total = total

    return context