from django.contrib import admin
from .models import *

# Register your models here.
#admin.site.register(Product)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)