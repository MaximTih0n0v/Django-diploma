from django.contrib import admin
from apps.products.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'price', 'discount', 'category', 'quantity']
    list_editable = ['price', 'discount']
    search_fields = ['name']
    list_filter = ['category', 'price']
