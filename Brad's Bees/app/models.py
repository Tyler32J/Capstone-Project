from django.db import models

# Create your models here.
STATE_CHOICES = []
class Product(models.Model):
    name = models.CharField(max_length=50)
    variant = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField()
    stock = models.PositiveIntegerField()
    is_acive = models.BooleanField(default=True)



class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2,
                             choices=STATE_CHOICES, # write or pip somehow
                             default="")
    zip_code = models.CharField(max_length=5)

    latitude = models.FloatField()
    longitude = models.FloatField()



class Order(models.Model):
    DELIVERY = "delivery"
    PICKUP = "pickup"

    FULFILLMENT_CHOICES = [
        (DELIVERY, "delivery"),
        (PICKUP, "pickup"),
    ]

    #-- customer info --#
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name="order")

    #-- order info --#
    fulfillment_method = models.CharField(max_length=10,
                                          choices=FULFILLMENT_CHOICES,
                                          default="")
    total_price = models.DecimalField()
    created_at = models.DateTimeField()



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="order_items")

    quantity = models.PositiveIntegerField()
    price = models.DecimalField()



# business settings and import geopy for them