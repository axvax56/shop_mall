from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product/%Y/%m/%d', default='')
    stock = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'my_product'
        verbose_name = '상품'
        verbose_name_plural = '상품'
