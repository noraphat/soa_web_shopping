from django.urls import path, include
from .views import Home , About , Contact , Product , AddProduct , ItemProduct
urlpatterns = [
    path('', Home,name='home-page'),
    path('about/', About,name='about-page'),
    path('contact/', Contact,name='contact-page'),
    path('product/', Product,name='product-page'),
    path('add_product/', AddProduct,name='addproduct-page'),
    path('all_product/', ItemProduct,name='allproduct-page'),
]