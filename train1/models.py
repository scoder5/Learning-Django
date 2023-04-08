from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    rollno = models.IntegerField()
    photo = models.ImageField(upload_to='media/student/%Y/%m/%d')
    sem = models.IntegerField()
    about = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    product_id = models.IntegerField()
    is_featured = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='media/product/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name