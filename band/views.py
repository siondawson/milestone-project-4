from django.shortcuts import render
from .models import Concert, Member
from .forms import ConcertForm

# Create your views here.

def index(request):
    """ a view to return the index page """
    concerts = Concert.objects.all()
    context = {
        'concerts': concerts
    }
    return render(request, 'band/index.html', context)


def about(request):
    """ a view to return the about page """
    members = Member.objects.all()
    context = {
        'members': members
    }
    return render(request, 'band/about.html', context)
    

def add_concert(request):
    """ Add a concert to the listings on home page """

    form = ConcertForm()
    template = 'band/add_concert.html'
    context = {
        'form': form,
    }

    return render(request, template, context)