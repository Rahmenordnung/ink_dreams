from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .models import Book, OrderItem, Order
from django.utils import timezone


def products(request):
    context = {
        'items': Book.objects.all()
    }
    return render(request, "book_detail.html", context)


def checkout(request):
    return render(request, "checkout.html")

class HomeView(ListView):
    model = Book
    paginate_by = 10
    template_name = "home.html"

class BookDetailView(DetailView): 
    model = Book
    template_name = "book_detail.html"
    
def add_book_to_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    ) 
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        #chech if the book is already in the order 
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("book:book_detail", slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("book:book_detail", slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date) 
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
    return redirect("book:book_detail", slug=slug)

    
def remove_book_from_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed from your cart.")
            return redirect("book:book_detail", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("book:book_detail", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("book:book_detail", slug=slug)
    
            
                
