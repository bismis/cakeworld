from django.shortcuts import render
from .models import product
# Create your views here.
def index(request):
    products=product.objects.all()
    return render(request,'index.html',{'pr': products})


def details(request,product_id):
    singleproduct=product.objects.get(id=product_id)
    return render(request, "single_product.html",{'sp': singleproduct})