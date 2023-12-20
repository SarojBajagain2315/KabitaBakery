from django.db import models

# Create your models here.
class Category(models.Model):
    category_name= models.CharField(max_length=100, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    project_name=models.CharField(max_length=100)
    product_price=models.FloatField()
    stock=models.IntegerField()
    product_description=models.TextField()
    product_image=models.FileField(upload_to='static/uploads',null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Category=models.ForeignKey(Category,on_delete= models.CASCADE,null=True)

    def __str__(self):
        return self.project_name 

