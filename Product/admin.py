from django.contrib import admin
from .models import Catalog, Category, Product
# Register your models here.
@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}
	list_filter = ['catalog',]

@admin.register(Product)
class Product(admin.ModelAdmin):
	list_display = ['name','slug','price','available','qty','sold','created','updated']
	list_filter  = ['available','created','updated']
	list_editable =['price', 'available']
	prepopulated_fields = {'slug': ('name',)}

