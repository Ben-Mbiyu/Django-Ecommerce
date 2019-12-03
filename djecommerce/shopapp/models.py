from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# # Create your models here.
# class Profile(models.Model):
#     # user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(max_length=255, blank=True)
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()



class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    price = models.PositiveIntegerField()
    on_offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name;

    def getProducts():
        products = Product.objects.all()
        return products;

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name

# class Order(models.Model):
