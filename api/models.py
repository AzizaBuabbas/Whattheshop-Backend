from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class LanguageCourse(models.Model):
    title = models.CharField(max_length=120)
    course_overview = models.TextField()
    logo = models.ImageField(upload_to='Language_Course', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.title

class Order(models.Model):
    STATUS_CHOICES = (
        ('C', 'Cart'),
        ('O', 'Ordered'),
        ('D', 'Delivered'),
        ('X', 'Cancelled'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name="orders")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    def __str__(self):
        return str(self.id)

class CartItem(models.Model):
    title = models.ForeignKey(LanguageCourse, on_delete=models.CASCADE)
    cart = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(str(self.id )+ " Cart ID: "+ str(self.cart.id) + " Item name: "+ self.item.name)