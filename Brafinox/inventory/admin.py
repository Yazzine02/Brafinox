from django.contrib import admin
from .models import Product, Client, BL, Buy, Payment, Sell

# Register your models here.
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(Sell)
admin.site.register(Buy)
admin.site.register(Payment)
admin.site.register(BL)