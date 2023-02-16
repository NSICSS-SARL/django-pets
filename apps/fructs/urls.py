from django.urls import path, include
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('suscribe', views.suscribe, name='suscribe'),
    path('about', views.about, name='about'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('slider', views.slider, name='slider'),
    path('shop', views.shop, name='shop'),
    path('news', views.news, name='news'),   
    path('singleproduct/<str:slug>', views.singleproduct, name='singleproduct'),
]