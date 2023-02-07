from django.urls import path, include
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('slider', views.slider, name='slider'),
    path('shop', views.shop, name='shop'),
    path('news', views.news, name='news'),    
    path('singlenews', views.singlenews, name='singlenews'),
    path('singleproduct/<str:nom>', views.singleproduct, name='singleproduct'),
]