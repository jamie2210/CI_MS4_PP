from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def view_favourites(request):
    """ A view to return the favourites page """
    return render(request, 'favourites/favourites.html')
