    
from django.urls import path
from .views import (
    BookDetailView,
    checkout,
    HomeView,
    add_book_to_cart,
    remove_book_from_cart
)

app_name = 'book'

urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('book_detail/<slug>/', BookDetailView.as_view(), name='book_detail'),
    path('add_book_to_cart/<slug>/', add_book_to_cart, name='add_book_to_cart'),
    path('remove_book_from_cart/<slug>/', remove_book_from_cart, name='remove_book_from_cart')
]