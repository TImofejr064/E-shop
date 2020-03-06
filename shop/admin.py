from django.contrib import admin
from .models import *

admin.site.register(Basket)
admin.site.register(BasketsItem)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Status)