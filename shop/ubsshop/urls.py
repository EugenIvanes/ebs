from django.conf.urls.static import static
from django import views
from django.conf import settings
from django.urls import path
from . import views
urlpatterns = [
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('view/<str:pk>/',views.view,name='view'),
    path('update_item/',views.updateItem, name='update_item'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
