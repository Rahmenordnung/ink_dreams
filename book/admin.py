from django.contrib import admin
from .models import Author, Book, OrderItem, Order, Payment

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Payment)


