from django.contrib import admin
from .models import ShopProfile

# Register your models here.

@admin.register(ShopProfile)
class ShopProfileAdmin(admin.ModelAdmin):
    pass