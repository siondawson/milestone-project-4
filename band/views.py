from django.shortcuts import render
from .models import Concert, Member

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
    