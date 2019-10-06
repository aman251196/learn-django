import uuid

from django.db import models
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class Product(BaseModel):
    title       = models.CharField(max_length = 120, null=False, blank=False)
    description = models.TextField()
    price       = models.DecimalField(null=False, blank=False, max_digits=1000, decimal_places=2)
    summary     = models.TextField(default="This stuff is really cool")

    @property
    def representation(self):
        return "Name: {}".format(self.title)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.representation
     
