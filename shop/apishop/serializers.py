from pyexpat import model
from attr import field, fields
from rest_framework import serializers
from .models import Products,PostImage

class ProductList(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            'name', 
            'price',
            'image'
        ]
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['id','images']
class ProductDescription(serializers.ModelSerializer):

    
    postimage_set = ImageSerializer(many=True)
   
    class Meta:
        model = Products
        fields = ['name','price','description','date','image','postimage_set']
class CrudSerealizator(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['name','sku','price','description']




  

        
