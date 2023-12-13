from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from datetime import datetime
from .models import Concert, Member
from .forms import ConcertForm


def index(request):
    """A view to return the index page"""
    today = timezone.now().date()
    concerts = Concert.objects.filter(date__gte=today).order_by('date')

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
    """ Add a concert to the listings on the home page """
    if request.method == 'POST':
        form = ConcertForm(request.POST)
        if form.is_valid():
            concert_date = form.cleaned_data['date']
            today = datetime.now().date()  # Convert to date object

            if concert_date.date() < today:  # Ensure concert_date is a date object for comparison
                messages.warning(request, 'Concert date is in the past. The concert was not added.')
            else:
                form.save()
                messages.success(request, 'Concert added!')
                return redirect(reverse('band'))
        else:
            messages.error(request, 'Failed to add concert. Please check form validity.')
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
    