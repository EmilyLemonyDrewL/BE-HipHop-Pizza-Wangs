from django.db import models
from .user import User

class Order(models.Model):

    cashier = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=50)
    customer_phone = models.IntegerField()
    customer_email = models.EmailField(max_length=50)
    order_type = models.CharField(max_length=50)
    status = models.CharField(max_length=6)
    payment_type = models.CharField(max_length=50)
    date_of_order_closure = models.DateField(auto_now=False)
    tip_amount = models.IntegerField()
