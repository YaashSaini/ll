from django.contrib import admin
from .models import Vendor, UserProfile, Product

admin.site.register(Vendor)
admin.site.register(UserProfile)
admin.site.register(Product)
