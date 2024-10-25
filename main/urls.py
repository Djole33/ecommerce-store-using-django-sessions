from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('details/<int:id>/', views.details, name='details'),
   path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
   path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
   path('cart/', views.view_cart, name='view_cart'),
   path('make_order/', views.make_order, name='make_order'),
]
