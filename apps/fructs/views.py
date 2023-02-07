from django.shortcuts import render,  redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Categorie, Testimonial, Title
import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import re
from django.core.mail import send_mail
from .forms import *

from rest_framework import viewsets # new
from .serializers import TitleSerializer, TestimonialSerializer


# Create your views here.
def index(request):   
    context = {}
    context['testimonials']= Testimonial.objects.all()
    return render(request, 'fructs/index.html', context)


def about(request):
    context = {}
    context['testimonials']= Testimonial.objects.all()
    return render(request, 'fructs/about.html', context)


def cart(request):
    products = Product.objects.all()
    return render(request, 'fructs/cart.html', {'products': products})


def slider(request):
    return render(request, 'fructs/index_2.html')


def news(request):
    return render(request, 'fructs/news.html')


def shop(request):
    categories = Categorie.objects.all()
    products_list = Product.objects.all()
    # Pagination with 3 products per page
    paginator = Paginator(products_list, 3)
    page_number = request.GET.get('page', 1)
    products = paginator.page(page_number)
    return render(request, 'fructs/shop.html', {'products': products, 'categories': categories})


def singlenews(request):
    return render(request, 'fructs/single-news.html')


def singleproduct(request, nom):
    if nom:
        pdt = Product.objects.get(name=nom)
        family = Product.objects.filter(label=pdt.label)
        return render(request, 'fructs/single-product.html', {'pdt': pdt, 'products': list(family)})
    return render(request, 'fructs/single-product.html')


def checkout(request):
    return render(request, 'fructs/single-product.html')


def contact(request):
    return render(request, 'fructs/contact.html')


