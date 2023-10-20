from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Product(models.Model):
    name = models.CharField(_('product name'), max_length=255)
    description = models.TextField(_('product description'), null=True, blank=True)
    price = models.PositiveIntegerField(_('product price'))
    quantity = models.PositiveIntegerField(_('product quantity'))

