from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Sheetmusic, Category
from .forms import SheetmusicForm

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


@login_required
def add_sheetmusic(request):
    """ Add sheetmusic to store """

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('band'))

    if request.method == 'POST':
        form = SheetmusicForm(request.POST, request.FILES)
        if form.is_valid():
            sheetmusic = form.save()
            messages.success(request, 'Sheetmusic added to store!')
            return redirect(reverse('sheetmusic_detail', args=[sheetmusic.id]))
        else:
            messages.error(request, 'Failed to add sheetmusic. Please ensure form is valid and try again.')
    else:
        form = SheetmusicForm()
        
    template = 'sheet_music/add_sheetmusic.html'
    context = {
        'form': form
    }

    return render(request, template, context)

@login_required
def edit_sheetmusic(request, sheetmusic_id):
    """ A view to edit sheetmusic """

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('band'))

    sheetmusic = get_object_or_404(Sheetmusic, pk=sheetmusic_id)

    if request.method == 'POST':
        form = SheetmusicForm(request.POST, request.FILES, instance=sheetmusic)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated sheetmusic!')
            return redirect(reverse('sheetmusic_detail', args=[sheetmusic.id]))
        else:
            messages.error(request, 'Failed to update sheetmusic. Please ensure form is valid')
    else:    
        form = SheetmusicForm(instance=sheetmusic)
        messages.info(request, f'You are editing {sheetmusic.name}')

    template = 'sheet_music/edit_sheetmusic.html'
    context = {
        'form': form,
        'sheetmusic': sheetmusic,
    }

    return render(request, template, context)

@login_required
def delete_sheetmusic(request, sheetmusic_id):
    """A view for deleting sheet music from the store"""

    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse('band'))

    sheetmusic = get_object_or_404(Sheetmusic, pk=sheetmusic_id)
    sheetmusic.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('sheetmusic'))
