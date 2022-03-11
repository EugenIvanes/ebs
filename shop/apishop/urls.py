from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.ProductListView.as_view()),
    path('description/',views.ProductDescriptionView.as_view(),name='detail'),
    path('read/<str:pk>/',views.read,name = "Read"),
    path('create/',views.create,name = "Create"),
    path('update/<str:pk>/',views.update,name = "Update"),
    path('delete/<str:pk>/',views.delete,name = "Delete"),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
