from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    lastUpdate = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.IntegerField()
    birthDate = models.DateField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
