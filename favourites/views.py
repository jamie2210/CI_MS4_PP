from django.shortcuts import render

# Create your views here.


def view_favourites(request):
    """ A view to return the favourites page """
    return render(request, 'favourites/favourites.html')
