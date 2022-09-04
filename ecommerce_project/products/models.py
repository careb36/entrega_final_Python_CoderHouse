from django.db import models
class Products(models.Model):
        name = models.CharField(max_length=50)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        description = models.CharField(max_length=200)
        stock = models.IntegerField()
        size = models.CharField(max_length=5)  # S, M, L, XL, XXL
        available = models.BooleanField(default=True)
        image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)
        class Meta:
                verbose_name = 'product'
                verbose_name_plural = 'products'

def __str__(self):
        return self.name

