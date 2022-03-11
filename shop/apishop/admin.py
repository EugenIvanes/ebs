from turtle import title
from django.contrib import admin
from .models import Products,PostImage


class PostImageAdmin(admin.StackedInline):
    model = PostImage
 
@admin.register(Products)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
 
    class Meta:
       model = Products
 

# Register your models here.
#admin.site.register(Products)

