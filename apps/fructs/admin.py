from django.contrib import admin
from .models import Product, Categorie, Unitie, Breadcumb

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "image", "label", "unite")

admin.site.register(Product, ProductAdmin)
admin.site.register(Categorie)
admin.site.register(Unitie)
admin.site.register(Breadcumb)


