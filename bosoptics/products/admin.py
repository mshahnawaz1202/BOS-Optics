from django.contrib import admin
from .models import Category, Brand, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'is_featured', 'is_new_arrival', 'is_best_seller')
    list_filter = ('category', 'brand', 'is_featured', 'is_new_arrival', 'is_best_seller')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
