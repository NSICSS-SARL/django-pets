from django.shortcuts import render,  redirect
from django.core.paginator import Paginator

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Product, Categorie, Testimonial, Title, Location, Breadcumb
from sendgrid.helpers.mail import Mail
from django.core.mail import send_mail
from .forms import *


def setContext():
    context = {}
    products_list = Product.objects.all()
    context['titles']= Title.objects.all()
    context['filtered'] = [x for x in products_list if x.isDemo == True]
    context['products'] = [x for x in products_list if x.isDemo == False]    
    context['testimonials']= Testimonial.objects.all()    
    context['categories'] = Categorie.objects.all()
    context['demo'] = products_list[:3]
    addresses = Location.objects.all()
    context['location'] = addresses[0]
    return context

context = setContext()

# Create your views here.
def index(request):
    # Pagination with 3 posts per page
    paginator = Paginator(context['filtered'], 3)
    page_number = request.GET.get('page', 1)           
    context['filtered'] = paginator.page(page_number)
    return render(request, 'fructs/index.html', context)


def about(request):
    context['breadcumb'] = Breadcumb.objects.get(slug='about')
    return render(request, 'fructs/about.html', context)

def cart(request):
    context['breadcumb'] = Breadcumb.objects.get(slug='cart')    
    return render(request, 'fructs/cart.html', context)

def slider(request):
    return render(request, 'fructs/index_2.html', context)

def news(request):
    context['breadcumb'] = Breadcumb.objects.get(slug='news')
    return render(request, 'fructs/news.html', context)
    
def suscribe(request):
    if request.method =='POST':
        pass

def shop(request):
    products_list = Product.objects.all()
    context['products'] = products_list.exclude(isDemo=True)  
    # Pagination with 3 posts per page
    paginator = Paginator(context['products'], 3)
    page_number = request.GET.get('page', 1)           
    context['products'] = paginator.page(page_number)
    context['breadcumb'] = Breadcumb.objects.get(slug='shop')
    return render(request, 'fructs/shop.html', context)

def singleproduct(request, slug):
    if slug:
        pdt = Product.objects.get(slug=slug)
        family = Product.objects.filter(label=pdt.label)
        context['products'], context['pdt']  = list(family), pdt       
        return render(request, 'fructs/single-product.html', context)
    return render(request, 'fructs/single-product.html')

def checkout(request):
    context['breadcumb'] = Breadcumb.objects.get(slug='checkout')
    return render(request, 'fructs/single-product.html', context)


def contact(request):
    context['breadcumb'] = Breadcumb.objects.get(slug='contact')    
    return render(request, 'fructs/contact.html', context)

def send_email(request):
  if request.method == 'POST':
    # Form was submitted
    form = EmailPostForm(request.POST)
    if form.is_valid():
      # Form fields passed validation
      cd = form.cleaned_data



