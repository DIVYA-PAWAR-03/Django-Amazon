from django.urls import path
from fashion import views

urlpatterns = [
    path('', views.product_detail, name='product_detail'),
    path('update_product/<int:id>/', views.update_product, name='update_product'),
    path('delete_product/<int:id>', views.delete_product, name='delete_product'),
]