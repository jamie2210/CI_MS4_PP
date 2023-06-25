from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Favourites(models.Model):
    """
    This model is for a user's favourites list
    """
    products = models.ManyToManyField(
        Product,
        blank=True
    )
    username = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    def __stry__(self):
        return f"{self.username}'s Favourites"
