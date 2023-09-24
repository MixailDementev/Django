from django.urls import path
from .views import total_in_db, total_in_view, total_in_template, upload_image
from . import views

urlpatterns = [
    path('db/', total_in_db, name='db'),
    path('view/', total_in_view, name='view'),
    path('template/', total_in_template, name='template'),
    path('upload/', upload_image, name='upload_image'),
    path('products/', views.get_all_products, name='products'),
    path('change_product/<int:product_id>/', views.change_product, name='change_product'),
]