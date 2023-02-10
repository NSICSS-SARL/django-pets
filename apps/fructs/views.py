from django.shortcuts import render,  redirect
from django.core.paginator import Paginator

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Categorie, Testimonial, Title, Location
from sendgrid.helpers.mail import Mail
import re
from django.core.mail import send_mail
from .forms import *

from rest_framework import viewsets # new
from .serializers import TitleSerializer, TestimonialSerializer

def setContext():
    context = {}
    products_list = Product.objects.all()
    context['titles']= Title.objects.all()
    filtered = [x for x in products_list if x.isDemo is True]
    context['filtered'] = filtered    
    products_list = [x for x in products_list if x.isDemo == False]    
    context['testimonials']= Testimonial.objects.all()
    context['products'] =  products_list
    context['categories'] = Categorie.objects.all()
    context['demo'] = products_list[:3]
    addresses = Location.objects.all()
    context['location']=addresses[0]
    return context

context = setContext()

# Create your views here.
def index(request):
    return render(request, 'fructs/index.html', context)


def about(request):    
    return render(request, 'fructs/about.html', context)


def cart(request):    
    return render(request, 'fructs/cart.html', context)


def slider(request):
    return render(request, 'fructs/index_2.html', context)


def news(request):
    return render(request, 'fructs/news.html', context)
    
def suscribe(request):
    if request.method =='POST':
        pass
        


def shop(request):
    context['products'] = Product.objects.all()
    page_number = request.GET.get('page', 1)
    # Pagination with 3 products per page
    
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
page_number = request.GET.get('page', 1)
posts = paginator.page(page_number)
    paginator = Paginator(context['products'], 3)        
    context['products'] = paginator.page(page_number)
    return render(request, 'fructs/shop.html', context)


def singleproduct(request, nom):
    if nom:
        name = name.lower()
        pdt = Product.objects.get(name=nom)
        family = Product.objects.filter(label=pdt.label)
        context['products'] = list(family)
        context['pdt'] = pdt       
        return render(request, 'fructs/single-product.html', context)
    return render(request, 'fructs/single-product.html')


def checkout(request):
    return render(request, 'fructs/single-product.html', context)


def contact(request):
    return render(request, 'fructs/contact.html', context)


