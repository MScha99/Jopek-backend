from django.contrib import admin

"""
admin.py w Django służy do rejestrowania modeli w interfejsie administracyjnym Django
Interfejs administracyjny Django jest wbudowaną funkcjonalnością, która umożliwia zarządzanie zawartością bazy danych za pomocą przeglądarki internetowej
"""


from .models import Category, Product, Comment, Profile, Order, OrderProduct, RentProduct

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    

@admin.register(Product)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','id', 'stock', "renteduntill","displayrent", 'slug']
    
    
    

@admin.register(Comment)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'created_on']
   
@admin.register(Profile)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ['id','user']

@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']
@admin.register(OrderProduct)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']

@admin.register(RentProduct)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id']
