from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restro(models.Model): #this is to create a new model for retaurant.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'restaurant')  # OneToOneField  is to ensure that one user have only one restarant.
    name = models.CharField(max_length = 500)
    phone = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='restaurant_logo/' , blank=False)

    def __str__(self) :
        return self.name