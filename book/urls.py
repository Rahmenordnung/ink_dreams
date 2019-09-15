    
from django.urls import path
from .views import (BookDetailView,
    CheckoutView,
    HomeView,
    add_book_to_cart,
    remove_book_from_cart,
    remove_one_book_from_cart,
    OrderFinalView,
    PaymentView
)

app_name = 'book'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order_final_view/', OrderFinalView.as_view(), name='order_final_view'),
    path('book_detail/<slug>/', BookDetailView.as_view(), name='book_detail'),
    path('add_book_to_cart/<slug>/', add_book_to_cart, name='add_book_to_cart'),
    path('remove_book_from_cart/<slug>/', remove_book_from_cart, name='remove_book_from_cart'),
    path('remove_one_book_from_cart/<slug>/', remove_one_book_from_cart, name='remove_one_book_from_cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    
]