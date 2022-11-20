from cgi import print_exception
from sre_constants import CATEGORY_UNI_DIGIT
from tokenize import Name
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models import F
from django.utils import timezone
from datetime import datetime, date, timedelta
   





class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
     return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)    
    price = models.IntegerField()
    brand = models.CharField(max_length=50)
    description =models.TextField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True) 
    category = models.ManyToManyField(Category, blank=True)
    slug = models.SlugField(max_length=20)
    image =models.ImageField(upload_to='images/', null=True, blank=True)
    displayrent = models.BooleanField(default=False) ##czy pokazywać jako opcja w wypożyczalni
    renteduntill = models.DateField(null=True, blank=True)

    
    
    
    def __str__(self):
     return self.name



class Comment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.owner)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
     return self.user.username

class Order(models.Model):  
    owner = models.ForeignKey(Profile, related_name='order', on_delete=models.PROTECT)
    order_date = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)
    price =models.IntegerField()
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)
    status = models.CharField(default="Oczekuje na akceptacje",max_length=40)
   
  

    def __str__(self):
     return self.notes
    
class OrderProduct(models.Model):
    id = models.BigAutoField(primary_key = True)
    order = models.ForeignKey(Order, related_name='OrderProduct', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='OrderProduct',on_delete=models.PROTECT)  
    quantity = models.IntegerField(default=1)

@receiver(post_save, sender=OrderProduct)
def create_order_product(sender, instance, created, **kwargs):
    if created:
         Product.objects.filter(id=instance.product.id).update(stock =F('stock') - instance.quantity)





class RentProduct(models.Model):
    id = models.BigAutoField(primary_key = True)
    owner = models.ForeignKey(Profile, null=True, blank=True, related_name='RentProduct', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='RentProduct',on_delete=models.PROTECT)  
    
@receiver(post_save, sender=RentProduct)
def create_order_product(sender, instance, created, **kwargs):
    if created:
         Product.objects.filter(id=instance.product.id).update(renteduntill = date.today()+ timedelta(days=7))

    
        
    
