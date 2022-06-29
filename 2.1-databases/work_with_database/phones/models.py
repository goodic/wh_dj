from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    name = models.CharField(max_length=254, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=1)
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Phone, self).save(*args, **kwargs)
