from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Sheetmusic, Category

# Create your views here.

def all_sheetmusic(request): 
    """A view to return all sheetmusic"""
    allsheetmusic = Sheetmusic.objects.all()
    query = None
    category = None

    if request.GET:

        if 'category' in request.GET:
            categories = request.GET['category']
            sheetmusic = allsheetmusic.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('sheetmusic'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            sheetmusic = allsheetmusic.filter(queries)

    context = {
        'allsheetmusic': allsheetmusic,
        'search_term': query,
        'current_categories': categories,
        }

    return render(request, 'sheet_music/sheetmusic.html', context)


def sheetmusic_detail(request, sheetmusic_id): 
    """A view to return individual sheet music details """
    sheetmusic = get_object_or_404(Sheetmusic, pk=sheetmusic_id)
    context = {
        'sheetmusic': sheetmusic
        }
    return render(request, 'sheet_music/sheetmusic_detail.html', context)

