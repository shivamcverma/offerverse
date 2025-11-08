from random import random
from django.db import models

# Create your models here.
from django.db import models

PLATFORM_CHOICES = (
    ('amazon', 'Amazon'),
    ('flipkart', 'Flipkart'),
)

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=50)
    image_url = models.URLField()
    affiliate_link = models.URLField()
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, blank=True, null=True )

    def save(self, *args, **kwargs):
        if not self.platform:
            self.platform = random.choice(['amazon', 'flipkart'])
        super().save(*args, **kwargs)
