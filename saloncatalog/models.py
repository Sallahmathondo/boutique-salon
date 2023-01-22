from django.db import models
import datetime
from django.utils import timezone
# Create your models here.


class SalonName(models.Model):
    salon_name = models.CharField(max_length=50, unique=True,
                                  help_text='Enter a salon number (e.g.baraka )')

    def __str__(self):
        return self.salon_name


class Salon(models.Model):
    name= models.ForeignKey(SalonName, on_delete=models.RESTRICT)
    salon_name= models.CharField(max_length=50)
    salon_hairstyle= models.CharField(max_length=50, null=True)
    Booking_date = models.DateTimeField('date launched', null=True)
    price = models.IntegerField(default=0)

    KE_SHILLINGS = 'Kshs'
    DOLLAR = 'Dollar'
   
    CURRENCY_CHOICES = [
        (KE_SHILLINGS, 'Kenya Shillings'),
        (DOLLAR, 'US Dollars'),
       
    ]
    sale_currency = models.CharField(
        max_length=10, choices=CURRENCY_CHOICES, default=KE_SHILLINGS)
    sku = models.CharField(max_length=5, default=0000, null=False)

    def __str__(self):
        return f'{self.name} {self.salon_name} {self.sale_currency} {self.price}'
