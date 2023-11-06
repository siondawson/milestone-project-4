from django.shortcuts import render
from .models import Concert

# Create your views here.

def index(request):
    """ a view to return the index page """
    concerts = Concert.objects.all()
    context = {
        'concerts': concerts
    }
    return render(request, 'band/index.html', context)
    