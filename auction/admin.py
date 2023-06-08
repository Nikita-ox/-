from django.contrib import admin

from auction.models import Product, Purchase


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "title", "price", "status")
    search_fields = ("name",)


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ("customer", "item", "count")
    search_fields = ("customer",)
