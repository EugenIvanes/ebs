from django.db import models

# Create your models here.



class Products(models.Model):
    name = models.CharField('Название',max_length=30, db_index = True)
    sku = models.CharField('Единица складского учёта',max_length=12,db_index=True)
    price = models.IntegerField('цена')
    description = models.TextField('Описание')
    date = models.DateTimeField(("дата"), auto_now_add=True)
    image = models.ImageField(blank=True,null = True)
   
    def __str__(self):
        return self.name

 
class PostImage(models.Model):
    post = models.ForeignKey(Products, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to = 'images/',null = True)
 
    def __str__(self):
        return self.post.name

