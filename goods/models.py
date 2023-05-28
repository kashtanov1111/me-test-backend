from django.db import models


# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=100)
    supplier_name = models.CharField(max_length=300)
    supplier_address = models.CharField(max_length=300)
    supplier_phone = models.CharField(max_length=300)
    is_bulk = models.BooleanField()
    price = models.IntegerField()
    dt_of_license = models.DateField()
