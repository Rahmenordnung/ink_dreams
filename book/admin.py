from django.contrib import admin
from .models import Book, OrderItem, Order

admin.site.register(Book)
admin.site.register(OrderItem)
admin.site.register(Order)


