from django.shortcuts import render , redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.

def home(request):
    return render(request, 'fashion/home.html')

def product_detail(request):
    prod = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
    return render(request, 'fashion/product_detail.html' , {'prod':prod, 'form':form})


def update_product(request, id):
    prod = get_object_or_404(Product,id=id)
    form = ProductForm(instance=prod)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            form.save()
            return redirect('product_detail')
    return render(request, 'fashion/update_product.html',{'form':form})


def delete_product(request, id):
    prod = get_object_or_404(Product, id=id)
    prod.delete()
    return redirect('product_detail')
