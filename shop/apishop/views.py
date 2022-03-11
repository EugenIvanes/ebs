from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .models import Products
from .serializers import ProductList,ProductDescription,CrudSerealizator
# Create your views here.
class ProductListView(generics.ListCreateAPIView):
        queryset = Products.objects.all()
        serializer_class = ProductList
       

class ProductDescriptionView(generics.ListCreateAPIView):
        queryset = Products.objects.all()
        serializer_class = ProductDescription
        
@api_view(['Get'])
def read(request,pk):
    product = Products.objects.filter(id=pk)
    serealizator = CrudSerealizator(product,many = True)
    return Response(serealizator.data)


@api_view(['POST'])
def create(request):
	serializer = CrudSerealizator(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def update(request, pk):
	task = Products.objects.get(id=pk)
	serializer = CrudSerealizator(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, pk):
	task = Products.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')