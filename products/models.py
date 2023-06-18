from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(
        max_length=254
        )
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
        )

    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
        )

    name = models.CharField(
        max_length=254
        )

    description = models.TextField()

    feature = models.TextField(
        max_length=500,
        blank=True
    )

    feature2 = models.TextField(
        max_length=500,
        blank=True
    )

    has_sizes = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    price = models.DecimalField(
        max_digits=6, decimal_places=2)
    A4_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=14.99)
    A3_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=19.99)
    A2_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=24.99)
    A1_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=29.99)
    A0_price = models.DecimalField(
        max_digits=6, decimal_places=2, default=39.99)

    image_url = models.URLField(
        max_length=1024,
        null=True,
        blank=True
        )

    image = models.ImageField(
        null=True,
        blank=True)

    def __str__(self):
        return self.name
