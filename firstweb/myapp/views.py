from django.shortcuts import render
from django.http import HttpResponse
from .models import Allproduct
# Create your views here.

def Home(request):
    product1 = 'Android'
    product2 = 'iPhone'
    product3 = 'Huawei'
    context = {'product1':product1,
               'product2':product2,
               'product3':product3,}
    return render(request,'myapp/home.html',context)

def About(request):
    return render(request,'myapp/about_us.html')
    
def Contact(request):
    return render(request,'myapp/contact_us.html')

def Product(request):
    return render(request,'myapp/product.html')

def AddProduct(request):
    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        price = data.get('price')
        detail = data.get('detail')
        imageurl = data.get('imageurl')

        new = Allproduct()
        new.name = name
        new.price = price
        new.detail = detail
        new.imageurl = imageurl
        new.save()
    return render(request,'myapp/add_product.html')

def ItemProduct(request):
    product = Allproduct.objects.all()
    context = {'product' : product}
    return render(request,'myapp/allproduct.html',context)