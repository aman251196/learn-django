from django.db import models

# Create your models here.

class Product(models.Model):
    title       = models.CharField(max_length = 120, null=False, blank=False)
    description = models.TextField()
    price       = models.DecimalField(null=False, blank=False, max_digits=1000, decimal_places=2)
    summary     = models.TextField(default="This stuff is really cool")

    
     
