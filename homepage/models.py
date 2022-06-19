from django.db import models


class Products(models.Model):
    name = models.CharField(max_length= 200)
    price = models.PositiveIntegerField()
    desc = models.TextField(blank=True)
    image = models.ImageField(upload_to="productImage", blank=True, null=True)

    class Meta():
        verbose_name_plural = 'product'

    def __dir__(self) -> str:
       #return ('%s---------%s' % (self.id, self.name ))
        return (self.name)