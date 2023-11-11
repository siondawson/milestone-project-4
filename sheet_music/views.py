from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Sheetmusic, Category

# Create your views here.

def all_sheetmusic(request): 
    """A view to return all sheetmusic"""
    allsheetmusic = Sheetmusic.objects.all()
    query = None
    categories = None
    searched_sheetmusic = allsheetmusic
    filtered_allsheetmusic = None

    if request.GET:
        print("Get request made")
        if 'category' in request.GET:
            
            categories = request.GET['category'].split(',')
            print(categories)
            filtered_allsheetmusic = allsheetmusic.filter(category__name__in=categories)
            print(filtered_allsheetmusic)
            categories = Category.objects.filter(name__in=categories)
            print(categories)

        if 'q' in request.GET:
            print("Searched")
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('sheetmusic'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(composer_firstname__icontains=query) | Q(composer_lastname__icontains=query)
            searched_sheetmusic = searched_sheetmusic.filter(queries)
    else:
        print("No get request")

    context = {
        'allsheetmusic': allsheetmusic,
        'searched_sheetmusic': searched_sheetmusic,
        'filtered_sheetmusic' : filtered_allsheetmusic,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'sheet_music/sheetmusic.html', context)


def sheetmusic_detail(request, sheetmusic_id): 
    """A view to return individual sheet music details """
    sheetmusic = get_object_or_404(Sheetmusic, pk=sheetmusic_id)
    context = {
        'sheetmusic': sheetmusic,
        }
    return render(request, 'sheet_music/sheetmusic_detail.html', context)

