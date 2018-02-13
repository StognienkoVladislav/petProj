from django.db import models
from django.urls import reverse
# Create your models here.

class Order(models.Model):

    internalID = models.IntegerField(unique=True)
    orderCreationTime = models.CharField(max_length=120)
    merchantID = models.IntegerField()
    status = models.CharField(max_length=120)
    amount = models.CharField(max_length=50)
    currency = models.CharField(max_length=120)
    orderID = models.TextField()
    orderType = models.CharField(max_length=120)
    orderDescription = models.CharField(max_length=500)

    def get_absolute_url(self):
        return reverse('orders:detail', kwargs = {'pk' : self.internalID})



