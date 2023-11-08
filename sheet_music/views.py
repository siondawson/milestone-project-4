from django.shortcuts import render
from .models import Sheetmusic

# Create your views here.

def all_sheetmusic(request): 
    """A view to return all sheetmusic"""
    allsheetmusic = Sheetmusic.objects.all()
    context = {
        'allsheetmusic': allsheetmusic
        }
    return render(request, 'sheet_music/sheetmusic.html', context)

