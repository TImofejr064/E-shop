from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete

class Basket(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    elements = models.ManyToManyField("BasketsItem")

def CreateBasket(sender, instance, **kworgs):
    try:
        new_b = Basket(user=instance)
        new_b.save()
        print('Basket was created!')
    except:
        pass
    else:
        pass

def DeleteBasket(sender, instance, **kworgs):
    try:
        new_b = Basket.objects.get(user=instance)
        new_b.delete()
        print('Basket was deleted!')
    except:
        pass
    else:
        pass

post_save.connect(CreateBasket, sender=User)
post_delete.connect(DeleteBasket, sender=User)

class BasketsItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    num = models.IntegerField()

    def __str__(self):
        return f'{self.product}'    

class Product(models.Model):
    name = models.TextField()
    description = models.TextField()
    weight = models.IntegerField()
    price = models.IntegerField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products_pics')

    def __str__(self):
        return f'{self.name}'    

class Category(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'    

class Status(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.name}'