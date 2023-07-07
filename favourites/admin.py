# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal:
from .models import Favourites
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class FavouritesAdmin(admin.ModelAdmin):
    """
    Admin class for the Favourites model.
    """
    list_display = (
        'username',
    )
    search_fields = (
        'username',
    )
    list_filter = (
        'username',
    )
    ordering = ('-date',)


admin.site.register(Favourites, FavouritesAdmin)
