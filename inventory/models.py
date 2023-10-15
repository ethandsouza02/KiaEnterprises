from django.db import models
import uuid

# Create your models here.

# This lays down the description for Product Table.

class Product(models.Model):
    #'id' establishes Products relationships with all other models

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=256)
    price = models.PositiveIntegerField(null=False)
    hasSub = models.BooleanField(null=False)
    

    #Admin Panel Beutification
    def __str__(self):
        return self.name
    
    
# laying down description for Sub-Product table responsible for categorizing the products based on attributes such as color  
class SubProduct(Product):
    sub_quality = models.CharField(max_length=256)
    # Maps relationship of subproduct with Product using Product id (FOREIGN KEY)
    product = models.ForeignKey(to = Product, on_delete=models.CASCADE, related_name="subproducts")

    #Admin Panel Beutification
    def __str__(self):
        return self.name
    
    
class Image(models.Model):
    image = models.TextField(default="Test Image")
    #Maps image of the product to Product
    product = models.ForeignKey(to = Product, on_delete=models.CASCADE)

class Description(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Maps Description to Product using Product id
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    about = models.TextField(null = False)
    dimension = models.CharField(max_length=256)
    weight = models.PositiveIntegerField()
       
    #Admin Panel Beutification
    def __str__(self):
        return self.about
    
# Establishing Product Categories   
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(null=False, max_length=256)

    #Mapping Category Name to Product
    products = models.ForeignKey(to= Product, on_delete= models.DO_NOTHING)
    
    #Admin Panel Beutification
    def __str__(self):
        return self.name
    
    
    
    

    





    