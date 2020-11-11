from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from .models import Offers

# Create your views here.
def index(request):
    products = Product.objects.all()
    # return HttpResponse("hello world")
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse('new add')