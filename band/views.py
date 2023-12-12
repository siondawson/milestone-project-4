from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from datetime import date, timedelta
from .models import Concert, Member
from .forms import ConcertForm


def index(request):
    """ a view to return the index page """
    concerts = Concert.objects.all().order_by('date')
    startdate = date.today()
    enddate = startdate + timedelta(days=6)
    pastconcert = Concert.objects.filter(date__range=[startdate, enddate])
    print(pastconcert)
    print(concerts)
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
    if request.method == 'POST':
        form = ConcertForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Concert added!')
            return redirect(reverse('band'))
        else:
            messages.error(request, 'Failed to add concert. \
            Please check form is valid')
    else:
        form = ConcertForm()

    template = 'band/add_concert.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_concert(request, concert_id):
    """Edit a concert in the concert listings"""
    concert = get_object_or_404(Concert, pk=concert_id)
    if request.method == 'POST':
        form = ConcertForm(request.POST, instance=concert)
        if form.is_valid():
            form.save()
            messages.success(request, 'Concert edited!')
            return redirect(reverse('band'))
        else:
            messages.error(request, 'Concert not updated. \
            Please check form is valid.')
    else:
        form = ConcertForm(instance=concert)
        messages.info(request, 'You are editing a concert listing.')

    template = 'band/edit_concert.html'
    context = {
        'form': form,
        'concert': concert,
    }

    return render(request, template, context)


def delete_concert(request, concert_id):
    """Delete a concert from the listings"""
    concert = get_object_or_404(Concert, pk=concert_id)
    concert.delete()
    messages.success(request, 'Concert deleted!')
    return redirect(reverse('band'))
    