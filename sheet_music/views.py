from django.shortcuts import render, get_object_or_404
from .models import Sheetmusic

# Create your views here.

def all_sheetmusic(request): 
    """A view to return all sheetmusic"""
    allsheetmusic = Sheetmusic.objects.all()
    context = {
        'allsheetmusic': allsheetmusic
        }
    return render(request, 'sheet_music/sheetmusic.html', context)


def sheetmusic_detail(request, sheetmusic_id): 
    """A view to return individual sheet music details """
    sheetmusic = get_object_or_404(Sheetmusic, pk=sheetmusic_id)
    context = {
        'sheetmusic': sheetmusic
        }
    return render(request, 'sheet_music/sheetmusic_detail.html', context)

