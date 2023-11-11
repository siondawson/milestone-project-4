from decimal import Decimal
from django.conf import settings 
from django.shortcuts import get_object_or_404
from sheet_music.models import Sheetmusic

def basket_contents(request):  # context processor to make bag contents available ot whole application

    basket_items = []
    total = 0
    basket_count = 0
    basket = request.session.get('basket', {})

    for sheetmusic_id, quantity in basket.items():
        sheetmusic = get_object_or_404(Sheetmusic, pk=sheetmusic_id)
        total += quantity * sheetmusic.price
        basket_count += quantity
        basket_items.append({
            'sheetmusic_id': sheetmusic_id,
            'quantity': quantity,
            'sheetmusic': sheetmusic,
        })

    grand_total = total

    context = {
        'basket_items': basket_items,
        'total': total,
        'basket_count': basket_count,
        'grand_total': grand_total,
    }

    return context