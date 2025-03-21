# from django.db import models

# # Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.FloatField()
#     description = models.TextField()
    
#     def __str__(self):
#         return self.name  
    
    
    
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name
